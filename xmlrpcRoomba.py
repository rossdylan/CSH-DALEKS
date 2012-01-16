from hxRoomba import roombaController
import httplib
import xmlrpclib as xmlrpc
from SimpleXMLRPCServer import SimpleXMLRPCServer as xmlrpcserv
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
