from hxRoomba import roombaController
import pygame

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
							roomba.right()
						if axisData <= -0.90:
							roomba.left()

	except KeyboardInterrupt:
		j.quit()
