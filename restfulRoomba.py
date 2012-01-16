#!/usr/bin/python2.7
from hxRoomba import roombaController
from bottle import route, run, request, abort

class restfulRoombaServer():
	def __init__(self,port,tty,baud):
		self.port = port
		self.roomba = roombaController(tty,baud)

	def start(self):
		run('0.0.0.0',self.port)

	@route('/engage',method='POST')
	def engage(self):
		try:
			self.roomba.engage()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	@route('/forward',method='POST')
	def forward(self):
		try:
			self.roomba.forward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	@route('/backward',method='POST')
	def backward(self):
		try:
			self.roomba.backward()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	@route('/left',method='POST')
	def left(self):
		try:
			self.roomba.left()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	@route('/right',method='POST')
	def right(self):
		try:
			self.roomba.right()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Issue communicating with the hardware')

	@route('/stop',method='POST')
	def stop(self):
		try:
			self.roomba.stop()
		except Exception:
			print 'Error communicating with hardware'
			abort(503,'Error communicating with the hardware')

	@route('/speed',method='POST')
	def setspeed(self):
		data = request.body.readline()
		if not data:
			abort(400, 'No data recieved')
		else:
			try:
				data = int(data)
				self.roomba.setSpeed(data)
			except ValueError:
				abort(400,'Invalid data recieved')
			except Exception:
				abort(503,'Error communicating with the hardware')

	@route('/sensors/:id',method='GET')
	def sensors(self,id):
		try:
			return self.roomba.getSensorData(id)
		except Exception:
			print 'Error communicating with the hardware'
			abort(503,'Error communicating with the hardware')
