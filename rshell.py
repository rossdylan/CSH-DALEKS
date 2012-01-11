""" 
	Program: Roomba Interface Shell
	Date: 01/11/2012
	Author: Will Dignazio
	Description: 
		Simple shell program for running commands to 
		a roomba attached to the pc. Using the roomba functions
		provided in hxRoomba, this shell will allow a user to 
		create a controller object. The controller object, along
		with the methods provided, will allow users full control of 
		the roomba.
"""

from hxRoomba import *

""" Universal Shell Roomba Controller """
rshell_controller = None 
""" Shell Input Buffer """
input_args = ""
""" Command Dictionary """
commands = { 
		"shell" : None 
		}

def getInput():
	""" Gets the input from the user, fills the argument
	buffer, trys to run the first argument, finally clearing
	the buffer for the next input.  
	"""
	uin = raw_input("rshell:> ")
	print(uin)


if __name__ == "__main__":
	ttydev = raw_input("Roomba ttyX Path: ")
	baud = int(raw_input("Baud Rate: "))
	try:
		print("Creating Controller...")
		rcontroller = roombaController(ttydev, baud)
	except Exception as e: 
		print("Error: "+str(e))
	while True: 
		getInput()
	exit()
