from xmlrpcRoomba import networkRoombaController
import pygame
def average(nums):
	total = 0
	for num in nums:
		total += num
	return total / len(nums)

if __name__ == "__main__":
	roomba = networkRoombaController("tula.student.rit.edu",8080)
	roomba.engage()
	pygame.init()
	j = pygame.joystick.Joystick(0)
	j.init()
	turning = False
	movingForward = False
	movingBackward = False
	numZeros = 0
	lastSpeed = 0
	#axis 1: -1=forward, 1=backwards
	#axis 0: -1=strafe left, 1=strafe right
	#axis 2: -1=turn left, 1=turn right
	lastSpeedChange = 0
	try:
		while True:
			pygame.event.pump()
			#this loop is for button data
			for i in range(0,j.get_numbuttons()):
				buttonData = j.get_button(i)
				if buttonData != 0:
					if i == 1:
						roomba.engage()

			#this loop is for axis data
			for i in range(0, j.get_numaxes()):
				axisData = j.get_axis(i)
				if axisData == 0:
					numZeros += 1
				if axisData != 0:
					numZeros = 0
				#forward and backwards controls
				if axisData > 0.00 or axisData < 0.00:
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

					#control turning
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

					#speed controls
					if i == 3:
						#-1 = speed3
						#0 = speed2
						#1 = speed1
						if axisData < 0.00 and lastSpeed != 3:
							roomba.setSpeed(3)
							lastSpeed = 3
						elif axisData == 0.00 and lastSpeed != 2:
							roomba.setSpeed(2)
							lastSpeed = 2
						elif axisData > 0.00 and lastSpeed != 1:
							roomba.setSpeed(1)
							lastSpeed = 1
				#handle stopping the roomba when the joystick gets zeroed out
				elif axisData == 0.00 and (i == 0 or i == 2):
					try:
						if turning == True and i == 2 and numZeros > 3:
							print "Sending turning stop"
							roomba.stop()
							turning = False
						if movingForward == True and i == 0 and numZeros > 3:
							print "sending forward stop"
							roomba.stop()
							movingForward = False
						if movingBackward == True and i == 0 and numZeros > 3:
							print "sending backward stop"
							roomba.stop()
							movingBackward = False
					except Exception:
						continue

	except KeyboardInterrupt:
		j.quit()

