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
	currentSpeed = 0
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
						if axisData < 0.00:
							if movingForward == False:
								if axisData < 0.00 and axisData >= -0.30 and currentSpeed != 1:
									roomba.setSpeed(1)
									currentSpeed = 1
								elif axisData < -0.30 and axisData >= -0.60 and currentSpeed != 2:
									roomba.setSpeed(2)
									currentSpeed = 2
								elif axisData < -0.60 and axisData >= -1.00 and currentSpeed != 3:
									roomba.setSpeed(3)
									currentSpeed = 3

								roomba.forward()
								movingForward = True

						if axisData > 0.00:
							if movingBackward == False:
								if axisData < 0.00 and axisData >= 0.30 and currentSpeed != 1:
									roomba.setSpeed(1)
									currentSpeed = 1
								elif axisData < 0.30 and axisData >= 0.60 and currentSpeed != 2:
									roomba.setSpeed(2)
									currentSpeed = 2
								elif axisData < 0.60 and axisData >= 1.00 and currentSpeed != 3:
									roomba.setSpeed(3)
									currentSpeed = 3

								roomba.backward()
								movingBackward = True
					if i == 2:
						if axisData > 0.00:
							if turning == False:
								if axisData < 0.00 and axisData >= 0.30 and currentSpeed != 1:
									roomba.setSpeed(1)
									currentSpeed = 1
								elif axisData < 0.30 and axisData >= 0.60 and currentSpeed != 2:
									roomba.setSpeed(2)
									currentSpeed = 2
								elif axisData < 0.60 and axisData >= 1.00 and currentSpeed != 3:
									roomba.setSpeed(3)
									currentSpeed = 3
								roomba.right()
								turning = True

						if axisData < 0.00:
							if turning == False:
								if axisData < 0.00 and axisData >= -0.30 and currentSpeed != 1:
									roomba.setSpeed(1)
									currentSpeed = 1
								elif axisData < -0.30 and axisData >= -0.60 and currentSpeed != 2:
									roomba.setSpeed(2)
									currentSpeed = 2
								elif axisData < -0.60 and axisData >= -1.00 and currentSpeed != 3:
									roomba.setSpeed(3)
									currentSpeed = 3
								roomba.left()
								turning = True
				elif axisData == 0.00 and (i == 0 or i == 2):
					if turning == True and i == 2:
						print "Sending turning stop"
						roomba.stop()
						turning = False
						roomba.setSpeed(1)
						currentSpeed = 1
					if movingForward == True and i == 0:
						if zeroCount > 3:
							print "sending forward stop"
							roomba.stop()
							movingForward = False
							roomba.setSpeed(1)
							currentSpeed = 1
					if movingBackward == True and i == 0:
						invalid = False
						if zeroCount > 3:
							print "sending backward stop"
							roomba.stop()
							movingBackward = False
							roomba.setSpeed(1)
							currentSpeed = 1


	except KeyboardInterrupt:
		j.quit()
