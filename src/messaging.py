"""The messaging class coordinates with the main loop to provide scheduling and
event handling functions."""

from game import game
import bisect

msgdic = {}
timed_event_queue=[]

class Trigger(): 
	def __init__(self,function,args,looping=True):
		self.function=function
		self.args=args
		self.looping=looping
	def execute(self,args):
		self.function(*(self.args+args))
		
def propagate(e, args=()):
	"""Calls an event of type e with arguments args."""
	game.messaging.last_propagated=e
	try:
		triggers = msgdic[e]
	except KeyError: 
		return
	
	for trigger in triggers:
		trigger.execute(args)
		if not(trigger.looping):
			triggers.remove(element)
			
def accept(e, func, args=(), looping=True):
	"""When event e occurs, call func with args plus event args"""
	t=Trigger(func,args,looping)
	try:
		triggers = msgdic[e]
	except KeyError:
		triggers = []
		msgdic[e] = triggers
	triggers.append(t)
	
def accept_once(e, func, args=[]):
	"""When event e is propagated, func will be called with the propagation args, but only once."""
	accept(e, func, args, False)
	
def ignore(e, func):
    """Cancel a previously accepted e/func combination."""
    try:
		triggers = msgdic[e]
		for t in triggers:
			if t.function==func:
				triggers.remove(t)
    except KeyError: pass


#FOR GAME TIMES ONLY, DO NOT USE FOR GAMESYNC INDEPENDENT INTERFACE
class TimedCall():
	def __init__(self,func,time,argz):
		self.time=time
		self.func=func
		self.argz=argz
	def __cmp__(self,other):
		return cmp(self.time,other.time)
		
def call_later(func,time,argz=[]):
	bisect.insort_right(timed_event_queue, TimedCall(time,func,argz))
	
def call_after(func,duration,args=[]):
	call_later(func,game.game_time+duration,args)
	
def pump_messaging():
	q=game.game_time
	while len(timed_event_queue):
		r=timed_event_queue.pop(0)
		if r.time>=q:
			timed_event_queue.insert(0,r)
			game.game_time=q 
			return
		else:
			game.game_time=r.time
			r.function(*r.argz)
	game.game_time=q
