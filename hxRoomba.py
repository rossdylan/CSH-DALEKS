import serial
import icreatepyrobot as pyrobot
import xmlrpclib as xmlrpc
from SimpleXMLRPCServer import SimpleXMLRPCServer as xmlrpcserv
import httplib

class roombaController():
	def __init__(self,tty,baudRate):
		self.serialConn = serial.Serial(tty,baudRate)
		self.roomba = pyrobot.Roomba(self.serialConn)
		self.speed = pyrobot.VELOCITY_SLOW
		self.methodList = ('engage','right','left','forward','backward','setSpeed', 'stop', 'getSensorData','onCliff')

	def engage(self):
		self.roomba.Control()

	def right(self):
		self.roomba.TurnInPlace(self.speed,direction='cw')
		#time.sleep(0.5)
	def left(self):
		self.roomba.TurnInPlace(self.speed,direction='ccw')
		#time.sleep(0.5)
	def forward(self):
		self.roomba.DriveStraight(self.speed)
		#time.sleep(0.5)
	def backward(self):
		self.roomba.DriveStraight(self.speed * -1)
		#time.sleep(0.5)
	def setSpeed(self,speed):
		"""1,2,3: slow fast max"""
		if speed == 1:
			self.speed = pyrobot.VELOCITY_SLOW
		if speed == 2:
			self.speed = pyrobot.VELOCITY_FAST
		if speed == 3:
			self.speed = pyrobot.VELOCITY_MAX
	def stop(self):
		self.roomba.Stop()

	def getSensorData(self,sensor):
		self.roomba.sensors.Clear()
		self.roomba.sensors.GetAll()
		if sensor in self.roomba.sensors:
			return self.roomba.sensors[sensor]
		else:
			return None
	
	def onCliff(self):
		right = self.getSensorData('cliff-right')
		left = self.getSensorData('cliff-left')
		front_left = self.getSensorData('cliff-front-left')
		front_right = self.getSensorData('cliff-front-right')
		if right or left or front_left or front_right:
			return True
		else:
			return False

class networkRoombaServer(roombaController):
	def __init__(self,port,tty,baudRate):
		roombaController.__init__(self,tty,baudRate)
		self.port = port
		self.server = xmlrpcserv(("0.0.0.0",self.port),allow_none=True)
		for method in self.methodList:
			self.server.register_function(getattr(self,method),method)
		self.server.register_introspection_functions()
		self.server.serve_forever()

class TimeoutTransport(xmlrpc.Transport):
	timeout = 2.0
	def set_timeout(self, timeout):
		self.timeout = timeout
	def make_connection(self, host):
		h = httplib.HTTPConnection(host, timeout=self.timeout)
		return h

class networkRoombaController():
	def __init__(self,address,port):
		self.addr = address
		self.port = port
		t = TimeoutTransport()
		self.server = xmlrpc.Server("http://%s:%s" % (self.addr,self.port),transport=t)
		serverMethods = self.server.system.listMethods()
		for method in serverMethods:
			self.__dict__[method] = getattr(self.server,method)
