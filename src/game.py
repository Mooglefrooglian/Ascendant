class game():
	#Contains all shared resources and variables related to the running of the game. 
	VERSION = "0.0"

	clock=None
	
	#Frame delta is the time since last frame
	frame_time=0.04
	
	running=True #Set to false to QUIT
	
	#ACTUAL SYNCHRONIZED INGAME TIME, INDEPENDENT OF REALWORLD TIME
	game_time=0
	steps_per_second = 30
	step_interval = 1.0 / steps_per_second
	
	
	class graphics():
		window=None
		last_focused=True
		
	class messaging():
		last_propagated=""
