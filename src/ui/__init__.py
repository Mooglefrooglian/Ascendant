from game import game
import os, re, imp

game.graphics.uis = {}	

#Find all the UIs and load 'em up. One suspects a generic plugin system might simplify this?
#Also I'm not using glob BECAUSE IM NOT.
for path,dirs,files in os.walk("src/ui"): #NO I HAVE NO IDEA HOW PATHS WORK
	for f in files:
		if f.endswith(".py") and not f.startswith('__init__') and not f.startswith('ui.py'):
			name = re.sub(r'\.py$', '', f)
			print("Found UI " + name)
			u = imp.load_source(name, path + "/" + f) #We found a UI!
			u.init() #Call its init function!