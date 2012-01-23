import urllib2
from urllib import urlencode


class restfulRoombaClient():
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.baseurl = "http://%s:%s/" % (self.host, self.port)
		self.postURLs = {"forward": self.baseurl + "forward",
				"backward": self.baseurl + "backward",
				"right": self.baseurl + "right",
				"left": self.baseurl + "left",
				"setSpeed": self.baseurl + "speed",
				"stop": self.baseurl + "stop"}
		self.getURLs = {"getSensorData": self.baseurl + "sensors/"}

	"""Lets get all of our post commands done first (I guess post is appropriate here?
		never really Done rest API design before..."""
	def forward(self):
		urllib2.urlopen(self.postURLs['forward'],data=urlencode({'exterminate','humans'}))
	def backward(self):
		urllib2.urlopen(self.postURLs['backward'],data=urlencode({'exterminate','humans'}))
	def right(self):
		urllib2.urlopen(self.postURLs['right'],data=urlencode({'exterminate','humans'}))
	def left(self):
		urllib2.urlopen(self.postURLs['left'],data=urlencode({'exterminate','humans'}))
	def setSpeed(self,speed):
		urllib2.urlopen(self.postURLs['speed'],data=urlencode({'speed',speed}))
	def stop(self):
		urllib2.urlopen(self.postURLs['stop'],data=urlencode({'exterminate','humans'}))

	"""Time for our one and only get command"""
	def getSensorsData(self,sensor):
		return urllib2.urlopen(self.postURLs['getSensorData'] + sensor).read()
