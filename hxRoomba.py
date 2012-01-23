import serial
import icreatepyrobot as pyrobot

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
		self.engage()
		self.roomba.sensors.GetAll()
		return self.roomba.sensors[sensor]

