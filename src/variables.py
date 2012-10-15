class game():
	#Contains all variables related to the running of the game. 
	#Nicely structure them maybe?
	clock=None
	#Frame delta is the time since last frame
	frameDelta=0.04
	#1 for title screen and 2 for game?
	renderState=1
	class graphics():
		window=None
		
