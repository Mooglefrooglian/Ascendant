"""The messaging class coordinates with the main loop to provide scheduling and
event handling functions."""

from game import game
import bisect

msgdic = {}
timedEventQueue=[]


class Trigger(): 
	def __init__(self,function,args,looping=True):
		self.function=function
		self.args=args
		self.looping=looping
	def execute(self,args):
		self.function(*(self.args+args))
		
def propagate(astr, args=()):
	"""Sends an event of type astr with arguments args."""
	game.messaging.lastPropagated=astr
	try:
		alist = msgdic[astr]
	except KeyError: return
	for element in alist:
		element.execute(args)
		if not(element.looping):
			alist.remove(element)
def accept(astr, afunc,args=(),looping=True):
	"""When event astr occurs, call afunc with args plus event args"""
	t=Trigger(afunc,args,looping)
	try:
		alist = msgdic[astr]
	except KeyError:
		alist = []
		msgdic[astr] = alist
	alist.append(t)
	
def acceptOnce(astr,afunc,args=[]):
	"""When astr event is propagated, afunc will be called with the propagation args, but only once."""
	accept(astr,afunc,args,False)
	
def ignore(astr, afunc):
    """Cancel a previously accepted astr/afunc combination."""
    try:
		alist = msgdic[astr]
		for element in alist:
			if element.afunc==afunc:
				alist.remove(afunc)
    except KeyError: pass


#FOR GAME TIMES ONLY, DO NOT USE FOR GAMESYNC INDEPENDENT INTERFACE
class TimedCall():
	def __init__(self,func,time,argz):
		self.time=time
		self.func=func
		self.argz=argz
	def __cmp__(self,other):
		return cmp(self.time,other.time)
def callLater(func,time,argz=[]):
	bisect.insort_right(TimedCall(time,func,argz))
	
def callAfter(func,duration,args=[]):
	callLater(func,game.gametime+duration,args)
def pumpMessaging():
	q=game.gametime
	while True:
		r=timedEventQueue.pop(0)
		if r.time>=q:
			timedEventQueue.insert(0,r)
			game.gametime=q 
			return
		else:
			game.gametime=r.time
			r.func(*r.argz)
	game.gametime=q
