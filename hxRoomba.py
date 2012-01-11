import serial
import icreatepyrobot as pyrobot
import time

class roombaController():
	def __init__(self,tty,baudRate):
		self.serialConn = serial.Serial(tty,baudRate)
		self.roomba = pyrobot.Roomba(self.serialConn)
	def engage(self):
		self.roomba.Control()

	def right(self):
		self.roomba.TurnInPlace(pyrobot.VELOCITY_SLOW,direction='clockwise')
		time.sleep(0.5)
		self.roomba.Stop()

	def left(self):
		self.roomba.TurnInPlace(pyrobot.VELOCITY_SLOW,direction='counter-clockwise')
		time.sleep(0.5)
		self.roomba.Stop()

	def forward(self):
		self.roomba.DriveStraight(pyrobot.VELOCITY_SLOW)
		time.sleep(0.5)
		self.roomba.Stop()

if __name__ == "__main__":
	roomba = pyrobot.Roomba(serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=2))

	roomba.Control()
	roomba.sensors.GetAll()
	print roomba.sensors['charge']
	roomba.TurnInPlace(pyrobot.VELOCITY_SLOW,direction='counter-clockwise')
	roomba.DriveStraight(pyrobot.VELOCITY_SLOW)
	raw_input()
