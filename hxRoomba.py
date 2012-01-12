import serial
import icreatepyrobot as pyrobot
import time
import pygame

class roombaController():
	def __init__(self,tty,baudRate):
		self.serialConn = serial.Serial(tty,baudRate)
		self.roomba = pyrobot.Roomba(self.serialConn)
	def engage(self):
		self.roomba.Control()

	def right(self):
		self.roomba.TurnInPlace(pyrobot.VELOCITY_SLOW,direction='cw')
		time.sleep(0.5)
		self.roomba.Stop()

	def left(self):
		self.roomba.TurnInPlace(pyrobot.VELOCITY_SLOW,direction='ccw')
		time.sleep(0.5)
		self.roomba.Stop()

	def forward(self):
		self.roomba.DriveStraight(pyrobot.VELOCITY_SLOW)
		time.sleep(0.5)
		self.roomba.Stop()
	def backward(self):
		self.roomba.DriveStraight(pyrobot.VELOCITY_SLOW * -1)
		time.sleep(0.5)
		self.roomba.Stop()

if __name__ == "__main__":
	roomba = roombaController("/dev/ttyUSB0",115200)
	roomba.engage()
	pygame.init()
	j = pygame.joystick.Joystick(0)
	j.init()
	#axis 1: -1=forward, 1=backwards
	#axis 0: -1=strafe left, 1=strafe right
	#axis 2: -1=turn left, 1=turn right
	try:
		while True:
			pygame.event.pump()
			for i in range(0, j.get_numaxes()):
				axisData = j.get_axis(i)
				if axisData != 0.00:
					if i == 1:
						if axisData <= -0.90:
							roomba.forward()
						if axisData >= 0.90:
							roomba.backward()
					if i == 2:
						if axisData >= 0.90:
							roomba.left()
						if axisData <= -0.90:
							roomba.right()

	except KeyboardInterrupt:
		j.quit()
