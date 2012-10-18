#THIS IS JUST TO MAKE IT EASIER TO RUN FOR PEOPLE WHO DON'T LIKE INSTANTLY CLOSING COMMAND PROMPTS
#SAID PEOPLE MAY ALSO HAVE MANY PYTHON INSTALLATIONS AND SUCH
import traceback
import sys
import Tkinter, tkMessageBox
sys.stdout=open("error.log","w+")
from twisted.python import log
log.startLogging(sys.stdout)
try:
	import main
except SystemExit: pass
except:
	traceback.print_exc()
	root = Tkinter.Tk()
	root.withdraw() 
	tkMessageBox.showwarning("OH MY GOD WE'RE ALL GOING TO DIE","An exception has occurred. Please post the following on the official forums:\n"+traceback.format_exc())
	print("Press enter to exit")
	input()
	
	# python.exe main.py 1 (strictly server, 0 or 1) (port) (number of players) (player 1's IP address) ... (player n)
