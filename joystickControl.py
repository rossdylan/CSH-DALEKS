from hxRoomba import networkRoombaController
import pygame
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
	zeroCount = 0
	#axis 1: -1=forward, 1=backwards
	#axis 0: -1=strafe left, 1=strafe right
	#axis 2: -1=turn left, 1=turn right
	try:
		while True:
			pygame.event.pump()
			for i in range(0, j.get_numaxes()):
				axisData = j.get_axis(i)
				if i == 1:
					if axisData == 0.00:
						zeroCount += 1
					else:
						zeroCount = 0
				if axisData > 0.00 or axisData < 0.00:
					if i == 1:
						if axisData < -0.10:
							if movingForward == False:
								roomba.forward()
								movingForward = True

						if axisData > 0.10:
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
				elif axisData == 0.00 and (i == 0 or i == 2):
					if turning == True and i == 2:
						print "Sending turning stop"
						roomba.stop()
						turning = False
					if movingForward == True and i == 0:
						if zeroCount > 3:
							print "sending forward stop"
							roomba.stop()
							movingForward = False
					if movingBackward == True and i == 0:
						invalid = False
						if zeroCount > 3:
							print "sending backward stop"
							roomba.stop()
							movingBackward = False


	except KeyboardInterrupt:
		j.quit()
