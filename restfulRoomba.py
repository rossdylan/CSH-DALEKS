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
		"""Lock the roomba api so Only one user can use it at a time"""
		if self.locked == False:
			self.locked = True
			self.lockedBy = request.environ.get('REMOTE_ADDR')
	def unlock(self):
		"""Unlock the roomba api after usage"""
		if self.locked:
			if self.lockedBy == request.environ.get('REMOTE_ADDR'):
				self.locked = False

	def start(self):
		"""Start the server"""
		self.engage = route(self.engage)
		run(host='0.0.0.0',port=self.port)

	def engage(self):
		"""Put the roomba serial api into full mode (lets us send commands)"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.engage()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def forward(self):
		"""Move the roomba forward until stop() is called"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.forward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def backward(self):
		"""Move the roomba backward until stop() is called"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.backward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def left(self):
		"""turn the roomba CCW until stop() is called"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.left()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def right(self):
		"""turn the roomba CW until stop() is called"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.right()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	def stop(self):
		"""Stop the roomba if it is in motion"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			self.roomba.stop()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Error communicating with the hardware')

	def setspeed(self):
		"""Set the speed of the roomba
			1: slow
			2: fast
			3: OHGODOHGODOHGOD
		"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		data = int(request.forms.get('speed'))
		if not data:
			abort(400, 'No data recieved')
		else:
			try:
				data = int(data)
				print data
				self.roomba.setSpeed(data)
			except ValueError:
				abort(400,'Invalid data recieved')
			except Exception as e:
				abort(503,'Error communicating with the hardware %s', str(e))

	def sensors(self,id):
		"""retreieve data from a single sensor"""
		if self.locked and self.lockedBy != request.environ.get('REMOTE_ADDR'):
			abort(403,'This Roomba is in use')

		try:
			data = self.roomba.getSensorData(id.strip())
			return str(data)
		except Exception as e:
			print 'Error communicating with the hardware: %s' % str(e)
			abort(503,'Error communicating with the hardware: %s' % str(e))
