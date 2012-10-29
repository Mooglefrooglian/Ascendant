class game():
	#Contains all shared resources and variables related to the running of the game. 
	VERSION = "0.1"

	clock=None
	
	#Frame delta is the time since last frame
	frame_time=0.04
	
	running=True #Set to false to QUIT
	
	#ACTUAL SYNCHRONIZED INGAME TIME, INDEPENDENT OF REALWORLD TIME
	game_time=0
	steps_per_second = 30
	step_interval = 1.0 / steps_per_second
	
	
	class graphics():
		drawables=[]
		camera=None
		window=None
		base_ui=None
		uis = {}
		last_focused=True
		resolution_x=1000
		resolution_y=1000
		
	class messaging():
		last_propagated=""
