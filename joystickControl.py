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
	zeroCount = 0
	#axis 1: -1=forward, 1=backwards
	#axis 0: -1=strafe left, 1=strafe right
	#axis 2: -1=turn left, 1=turn right
	lastSpeedChange = 0
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
					if roomba.onCliff():
						roomba.engage()
					if i == 1:
						if axisData < 0.00:
							if movingForward == False:
								try:
									roomba.forward()
								except Exception:
									continue
								movingForward = True

						if axisData > 0.00:
							if movingBackward == False:
								try:
									roomba.backward()
								except Exception:
									continue
								movingBackward = True

					if i == 2:
						if axisData > 0.00:
							if turning == False:
								try:
									roomba.right()
								except Exception:
									continue
								turning = True

						if axisData < 0.00:
							if turning == False:
								try:
									roomba.left()
								except Exception:
									continue
								turning = True
					if i == 3:
						if math.fabs(lastSpeedChange - axisData) >= 0.5:
							try:
								if axisData == 0.00:
									roomba.setSpeed(2)
								if axisData >= 0.90:
									roomba.setSpeed(3)
								if axisData <= -0.90:
									roomba.setSpeed(1)
								lastSpeedChange = axisData
							except Exception:
								continue
				elif axisData == 0.00 and (i == 0 or i == 2):
					try:
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
					except Exception:
						continue

	except KeyboardInterrupt:
		j.quit()

