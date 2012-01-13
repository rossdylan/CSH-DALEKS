from hxRoomba import networkRoombaController
import pygame
import math
if __name__ == "__main__":
	roomba = networkRoombaController("tula.student.rit.edu",8080)
	roomba.engage()
	pygame.init()
	j = pygame.joystick.Joystick(0)
	j.init()
	turning = False
	movingForward = False
	movingBackward = False
	speedChanged = False
	lastSpeed = 0
	#axis 1: -1=forward, 1=backwards
	#axis 0: -1=strafe left, 1=strafe right
	#axis 2: -1=turn left, 1=turn right
	try:
		while True:
			pygame.event.pump()
			for i in range(0, j.get_numaxes()):
				axisData = j.get_axis(i)
				print i
				if axisData != 0.00:
					if i == 1:
						if axisData < 0.00:
							if movingForward == False:
								roomba.forward()
								movingForward = True

						if axisData > 0:
							if movingBackward == False:
								roomba.backward()
								movingBackward = True
					if i == 2:
						if axisData > 0.00:
							if turning == False:
								roomba.right()
								turning = True

						if axisData <= 0.00:
							if turning == False:
								roomba.left()
								turning = True
					if i == 3:
						if  math.fabs(lastSpeed - axisData) >= 0.90:
							speedChanged = False
						if speedChanged == False:
							if axisData > 0.00:
								roomba.setSpeed(3)
							if axisData == 0.00:
								roomba.setSpeed(2)
							if axisData < 0.00:
								roomba.setSpeed(1)
							speedChanged = True
				elif axisData == 0.00 and (i == 0 or i == 2):
					if turning == True:
						roomba.stop()
						turning = False
					if movingForward == True:
						roomba.stop()
						movingForward = False
					if movingBackward == True:
						roomba.stop()
						movingBackward = False


	except KeyboardInterrupt:
		j.quit()
