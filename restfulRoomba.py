#!/usr/bin/python2.7
from hxRoomba import roombaController
from bottle import route, run, request, abort

class restfulRoombaServer(object):

	def __new__(self, *args, **kwargs):
		obj = super(restfulRoombaServer, self).__new__(self,*args,**kwargs)
		route('/engage',method='POST')(obj.engage)
		route('/forward',method='POST')(obj.forward)
		route('/backward',method='POST')(obj.backward)
		route('/left',method='POST')(obj.left)
		route('/right',method='POST')(obj.right)
		route('/stop',method='POST')(obj.stop)
		route('/speed',method='POST')(obj.setspeed)
		route('/sensors/<id>',method='GET')(obj.sensors)
		return obj

	def __init__(self,port,tty,baud):
		self.port = port
		self.roomba = roombaController(tty,baud)

	def start(self):
		self.engage = route(self.engage)
		run(host='0.0.0.0',port=self.port)

	def engage(self):
		try:
			self.roomba.engage()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def forward(self):
		try:
			self.roomba.forward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def backward(self):
		try:
			self.roomba.backward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def left(self):
		try:
			self.roomba.left()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def right(self):
		try:
			self.roomba.right()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def stop(self):
		try:
			self.roomba.stop()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Error communicating with the hardware')

	def setspeed(self):
		data = int(request.forms.get('speed'))
		if not data:
			abort(400, 'No data recieved')
		else:
			try:
				data = int(data)
				self.roomba.setSpeed(data)
			except ValueError:
				abort(400,'Invalid data recieved')
			except Exception as e:
				abort(503,'Error communicating with the hardware %s', str(e))

	def sensors(self,id):
		try:
			data = self.roomba.getSensorData(id.strip())
			return str(data)
		except Exception as e:
			print 'Error communicating with the hardware: %s' % str(e)
			abort(503,'Error communicating with the hardware: %s' % str(e))
