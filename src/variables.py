class game():
	#Contains all variables related to the running of the game. 
	#Nicely structure them maybe?
	clock=None
	#Frame delta is the time since last frame
	frameTime=0.04
	running=True
	#ACTUAL SYNCHRONIZED INGAME TIME, INDEPENDENT OF REALWORLD TIME
	gametime=0
	class graphics():
		window=None
		lastFocused=True
	class messaging():
		lastPropagated=""
