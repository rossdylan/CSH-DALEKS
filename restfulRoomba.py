#!/usr/bin/python2.7
from hxRoomba import roombaController
from bottle import route, run, request, abort

class restfulRoombaServer(object):

	def __new__(self, *args, **kwargs):
		obj = super(restfulRoombaServer, self).__new__(self,*args,**kwargs)
		route('/lock',method='POST')(obj.lock)
		route('/unlock',method='POST')(obj.unlock)
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
		self.locked = False
		self.lockedBy = ""

	def lock(self):
		if self.locked == False:
			self.locked = True
			self.lockedBy = request.environ.get('REMOTE_ADDR')
	def unlock(self):
		if self.locked:
			if self.lockedBy == request.environ.get('REMOTE_ADDR'):
				self.locked = False

	def start(self):
		self.engage = route(self.engage)
		run(host='0.0.0.0',port=self.port)

	def engage(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.engage()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def forward(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.forward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def backward(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.backward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def left(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.left()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def right(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.right()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def stop(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.stop()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Error communicating with the hardware')

	def setspeed(self):
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

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
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			data = self.roomba.getSensorData(id.strip())
			return str(data)
		except Exception as e:
			print 'Error communicating with the hardware: %s' % str(e)
			abort(503,'Error communicating with the hardware: %s' % str(e))
