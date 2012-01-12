from hxRoomba import networkRoombaController
import pygame

if __name__ == "__main__":
	roomba = networkRoombaController("synapse.wireless.rit.edu",8080)
	roomba.engage()
	pygame.init()
	j = pygame.joystick.Joystick(0)
	j.init()
	moving = False
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
						if axisData < 0.00:
							if axisData < 0.00 and axisData >= -0.30:
								roomba.setSpeed(1)
							if axisData < -0.30 and axisData >= -0.60:
								roomba.setSpeed(2)
							else:
								roomba.setSpeed(3)
							roomba.forward()
							moving = True

						if axisData > 0:
							if axisData > 0 and axisData <= 0.30:
								roomba.setSpeed(1)
							if axisData > 0.30 and axisData <= 0.60:
								roomba.setSpeed(2)
							else:
								roomba.setSpeed(3)
							roomba.backward()
							moving = True
						elif axisData == 0.00:
							if moving == True:
								roomba.stop()
								moving = False
					if i == 2:
						if axisData > 0.00:
							if axisData > 0.00 and axisData <= 0.30:
								roomba.setSpeed(1)
							if axisData > 0.30 and axisData <= 0.60:
								roomba.setSpeed(2)
							else:
								roomba.setSpeed(3)
							roomba.right()
							moving = True

						if axisData <= 0.00:
							if axisData < 0.00 and axisData >= -0.30:
								roomba.setSpeed(1)
							if axisData < -0.30 and axisData >= -0.60:
								roomba.setSpeed(2)
							else:
								roomba.setSpeed(3)
							roomba.left()
							moving = True

						elif axisData == 0.00:
							if moving == True:
								roomba.stop()
								moving = False

	except KeyboardInterrupt:
		j.quit()
