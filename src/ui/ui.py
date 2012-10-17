"""	The purpose of a UI is to collect a bunch of interactive elements into one easy to use thing.
	For example, when a player opens the options window, the program should funnel
	all of the mouseclicks into it and ignore mouseclicks sent to the game.
	With this, one would simply create an OptionsUI and tell the game it's the top priority.
	This is probably nonsensical, so read onto the code!										"""
	
from game import game
import os, re
import messaging

class UI(object):
	"""The base UI class from which all other UI elements should be modelled after."""
	def __init__(self):
		self.events = [] #[event string, func] array representing what this UI responds to 
		#We could fill up this with like keys to quit and stuff like that (stuff that should work
		#anywhere in the application)
		
		self.children = [] #children of this UI element - they get a higher priority
		self.parent = None
		
	def begin_capture(self, block_other_input=False):
		for e in self.events:
			messaging.accept(e[0], e[1])
			
	def end_capture(self):
		for e in self.events:
			messaging.ignore(e[0], e[1])
		
	def add_child(self, c):
		self.children.append(c)
		c.begin_capture()
		
	def remove_child(self, c):
		self.children.remove(c)
		c.end_capture()
	
	def render(self):
		#This doesn't render a whole lot, as it is the base class!
		for c in self.children:
			c.render()