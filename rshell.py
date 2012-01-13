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

""" Shell's Roomba and Its Controller """
roomba_controller = None

def quit(args):
	""" Shell Command: 
		Quits the shell, saves no values. 
	"""
	print "rage quit"
	exit()

def shell_status(args):
	""" Prints the status of the shell, and 
	it's controllers. """
	print(roomba_controller)

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
		print("Made It Here")
		sub_com = args[1]
		try:
			shell_com = shell_commands[sub_com]
			shell_com(args)
		except KeyError as e: 
			print("Uknown Shell Command.")
	except IndexError as e: 
		pass

def connect(args):
	""" Connects the shell to the roomba 
	at the device specified, at the baud 
	rate specified. 
	"""
	try: 
		dev = args[1]
		print(dev)
		baud = int(args[2])
		print(baud)
		try: 
			print("Attempting To Connect To Roomba")
			roomba_controller = roombaController(dev,baud)
			print("Success.")
		except Exception as e: 
			print("An Error Has Occurred:\n")
	except Exception as e2: 
		print("Error:\n"+str(e2))

""" Command Dictionary """
commands = { 
		"quit" : quit,
		"shell" : shell, 
		"connect" : connect
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
	dev = raw_input("Roomba Device Location: ")
	baud = raw_input("Roomba Baud Rate: ")
	try: 
		roomba_controller = roombaController(dev,int(baud))
	except Exception as e: 
		print("Error Connecting To Roomba: "+str(e))
	
	while True: 
		getInput()

	exit()
