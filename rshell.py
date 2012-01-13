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

""" Universal Shell Roomba Controller List"""
roomba_controllers = []

def quit(args):
	""" Shell Command: 
		Quits the shell, saves no values. 
	"""
	print "rage quit"
	exit()

def shell_status(args):
	""" Prints the status of the shell, and 
	it's controllers. """
	pass

""" Shell Sub-Commands """
shell_commands = {
		"status" : shell_status 	#TODO: Write Print Status Function
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
		shell_commands["status"](args)
		
def connect(args):
	""" Connects the shell to the roomba 
	at the device specified, at the baud 
	rate specified. 
	"""
	try: 
		dev = args[0]
		print(dev)
		baud = int(args[1])
		print(baud)
		try: 
			controller = roombaController(dev,baud)
			roomba_controllers.append(controller)
		except Exception as e: 
			print("An Error Has Occurred:\n\t")
	except Exception as e2: 
		print("Error: "+str(e2))

""" Command Dictionary """
commands = { 
		"quit" : quit,
		"shell" : shell, 
		"connect" : connect
		}

def runcom(cstr, args):
	""" Recieves a string that is the command to run, 
	then will use it as a key in the command dictionary. 
	If the key is mapped, then the command there will be 
	executed. 
	"""
	try:
		com = commands[cstr]
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
	runcom(args[0], args[1:])

if __name__ == "__main__":
	while True: 
		getInput()
	exit()
