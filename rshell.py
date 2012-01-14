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

""" ################################################## """
""" ##############INITIALIZE ROOMBA################### """

""" Shell's Roomba and Its Controller """
roomba_controller = None	

dev = raw_input("Roomba Device Location: ")
baud = raw_input("Roomba Baud Rate: ")
try: 
	roomba_controller = roombaController(dev,int(baud))
except Exception as e: 
	print("Error Connecting To Roomba: "+str(e))
	exit()

""" ################################################## """

def quit(args):
	""" Shell Command: 
		Quits the shell, saves no values. 
	"""
	exit()

def shell_status(args):
	""" Prints the status of the shell, and 
	it's controllers. """
	print(roomba_controller)

def speed_stub(args):
	""" stub function to run the roomba's set speed command in hxRoomba. 
	The function requires an extra argument, and this stub handles it. """
	try:
		roomba_controller.setSpeed(args[2])
	except Exception as e: 
		print("Set Speed Error: " + str(e))

""" Roomba Commands """
roomba_commands = { 
		"engage"	: (False, getattr(roomba_controller, "engage")), 
		"right"		: (False, getattr(roomba_controller, "right")),
		"left"		: (False, getattr(roomba_controller, "left")),
		"forward"	: (False, getattr(roomba_controller, "forward")),
		"backward"	: (False, getattr(roomba_controller, "backward")),
		"stop"		: (False, getattr(roomba_controller, "stop")),
		"setspeed" 	: (True, speed_stub)
	}

def rCom(args): 
	""" Function to handle roomba commands, 
	essentially runs whatever string the user types 
	based on the roomba_commands dictionary. 
	"""
	try: 
		com = roomba_commands[args[1]]
		if com[0] == True:
			com[1](args)
		else:
			com[1]()
	except IndexError as e: 
		print("No Command")
	finally:
		pass

""" Shell Sub-Commands """
shell_commands = {
		"status" : shell_status 
		}

def shell(args): 
	""" Shell interface functions, if there is only one
	argument, it prints the status of the roomba shell and 
	controller status. The second argument is the sub command 
	that will print more specific shell values. 
	"""
	try: 
		sub_com = args[1]
		try:
			shell_com = shell_commands[sub_com]
			shell_com(args)
		except KeyError as e: 
			print("Uknown Shell Command.")
	except IndexError as e: 
		pass

""" Command Dictionary """
commands = { 
		"quit" : quit,
		"exit" : quit, 
		"shell" : shell, 
		"roomba" : rCom
		}

def runcom(args):
	""" Recieves a string that is the command to run, 
	then will use it as a key in the command dictionary. 
	If the key is mapped, then the command there will be 
	executed. 
	"""
	try:
		com = commands[args[0]]
		com(args)
	except KeyError as e:
		print "invalid command"

def getInput():
	""" Gets the input from the user, fills the argument
	buffer, trys to run the first argument, finally clearing
	the buffer for the next input.  
	"""
	uin = str(raw_input("rshell:> "))
	args = uin.split(" ") 
	runcom(args)

if __name__ == "__main__":
		
	while True: 
		getInput()

	exit()
