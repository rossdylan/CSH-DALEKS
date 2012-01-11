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
		"quit" : quit 
		"shell" : shell
		}
""" Shell Sub-Commands """
shell_commands = {
	"status" : None
	}
def shell(): 
	""" Shell interface functions, if there is only one
	argument, it prints the status of the roomba shell and 
	controller status. The second argument is the sub command 
	that will print more specific shell values. 
	"""

def quit():
	""" Shell Command: 
		Quits the shell, saves no values. 
	"""
	exit()

def runcom(cstr):
	""" Recieves a string that is the command to run, 
	then will use it as a key in the command dictionary. 
	If the key is mapped, then the command there will be 
	executed. 
	"""
	try:
		com = commands[cstr]
		com()
	except KeyError as e:
		print "invalid command"

def getInput():
	""" Gets the input from the user, fills the argument
	buffer, trys to run the first argument, finally clearing
	the buffer for the next input.  
	"""
	uin = str(raw_input("rshell:> "))
	input_args = uin.split(" ") 
	runcom(input_args[0])
	intput_args = []		# Cleared for next input string

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
