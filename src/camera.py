from game import game
import messaging
import pygame
import math

class Camera():
	"""Provides a 2d viewport into the game world."""
	def __init__(self,screenx,screeny,width,height):
		self.x=screenx
		self.y=screeny
		self.width=width
		self.height=height
		self.surface=pygame.Surface((width,height),pygame.SRCALPHA)
		#Cam_X and Cam_Y are the top left of the camera
		self.cam_x=0.0
		self.cam_y=0.0
		#Center_X and Center_Y are the camera's center
		self.center_x=0.0
		self.center_y=0.0
		#Used for mouse panning with middle mouse key
		self.pan_x,self.pan_y=0.0,0.0
		#Amounts of gameworld to render x/y 
		self.distance_x_base=self.distance_x=1.0
		self.distance_y_base=self.distance_y=height/float(width)
		#Stores scaled images for speed
		self.scaled_images_dict={}
		
		self.center(0.0,0.0)
		self.zoom(26)
		messaging.accept("new_frame",self.arrow_key_check)
		messaging.accept("5-5",self.mouse_scroll_out)
		messaging.accept("5-4",self.mouse_scroll_in)
		messaging.accept("5-2",self.mouse_pan_on)
		messaging.accept("6-2",self.mouse_pan_off)
		messaging.accept("left_click_down",self.check_terrain_click)
	def draw(self):
		game.graphics.window.blit(self.surface,(self.x,self.y))
	def arrow_key_check(self):
		"""Updates position of camera if arrow key is held down"""
		pressed=pygame.key.get_pressed()
		#Left arrow key
		xoff=yoff=0
		if pressed[276]:
			xoff-=1
		#Right arrow key
		if pressed[275]:
			xoff+=1
		#Up
		if pressed[273]:
			yoff-=1
		#Down
		if pressed[274]:
			yoff+=1
		if xoff!=0 or yoff!=0:
			self.reposition(self.cam_x+xoff*8*game.frame_time,self.cam_y+yoff*8*game.frame_time)
	def renderobject(self,x,y,image):
		"""Draws image at ingame coordinates x,y to screen"""
		x2,y2=self.world_to_render(float(x),float(y))
		scale=round(self.distance_x,1)
		if (image,scale) in self.scaled_images_dict:
			im=self.scaled_images_dict[(image,scale)]
		else:
			im=pygame.transform.smoothscale(image,(int(math.ceil(image.get_width()*(self.distance_x_base/self.distance_x))),int(math.ceil(image.get_height()*(self.distance_y_base/self.distance_y)))))
			self.scaled_images_dict[(image,scale)]=im
		self.surface.blit(im,(x2-im.get_width()/2.0,y2-im.get_height()/2.0))
	def screen_to_cam(self,x,y):
		"""Converts pixel on the screen to point ([0-1],[0-1]) on the camera."""
		return ((x-self.x)/self.width,(y-self.y)/self.height)
	def cam_to_screen(self,x,y):
		return (x*self.width+self.x,y*self.height+self.y)
	def cam_to_world(self,x,y):
		"""Converts a point on the 'camera' to a point on the 'world' (0,0) on the camera coordinates is top left, (1,1) is bottom right."""
		return (self.cam_x+x*self.distance_x,self.cam_y+y*self.distance_y)
	def world_to_cam(self,x,y):
		"""Converts a point on the world to a point on the camera."""
		return ((x-self.cam_x)/self.distance_x,(y-self.cam_y)/self.distance_y)
	def world_to_screen(self,x,y):
		x2,y2=self.world_to_cam(x,y)
		return self.cam_to_screen(x2,y2)
	def world_to_render(self,x,y):
		"""Converts point in world to point in render- pixels offset from top left of camera screen"""
		x2,y2=self.world_to_cam(x,y)
		return (x2*self.width,y2*self.height)
	def update(self):
		#Draw tiles
		#Get world coordinates of top left of camera
		start_x,start_y=self.cam_to_world(0,0)
		self.surface.fill((0,0,0))
		#Get world coordinates of bottom right of camera
		end_x,end_y=self.cam_to_world(1,1)
		#Draw everything
		for drawable in game.graphics.drawables:
			if drawable.x+drawable.image.get_width()>=start_x and drawable.y+drawable.image.get_height()>=start_y \
			and drawable.x-drawable.image.get_width()<=end_x and drawable.y-drawable.image.get_height()<=end_y:
				self.renderobject(drawable.x,drawable.y,drawable.image)
		self.draw()
	def center(self,x,y):
		self.cam_x=x-self.distance_x/2.0
		self.cam_y=y-self.distance_y/2.0
		self.center_x=x
		self.center_y=y
	def reposition(self,x,y):
		self.cam_x=x
		self.cam_y=y
		self.center_x=x+self.distance_x/2.0
		self.center_y=y+self.distance_y/2.0
	def zoom(self,level):
		if level<3: level=3
		if level>120: level=120
		cenx,ceny=self.center_x,self.center_y
		self.distance_y=level*(self.distance_y/self.distance_x)
		self.distance_x=level
		self.center(cenx,ceny)
	def mouse_scroll_out(self,event):
		x,y=event.pos
		if x>self.x and y>self.y and x<self.x+self.width and y<self.y+self.height:
			self.zoom(self.distance_x*1.2)
	def mouse_scroll_in(self,event):
		x,y=event.pos
		if x>self.x and y>self.y and x<self.x+self.width and y<self.y+self.height:
			x2,y2=self.screen_to_cam(x,y)
			x,y=self.cam_to_world(x2,y2)
			self.zoom(self.distance_x/1.2)
			self.center(x-(x2-0.5)*self.distance_x,y-(y2-0.5)*self.distance_y)
	def mouse_pan_on(self,event):
		self.pan_x,self.pan_y=event.pos
		messaging.accept("4",self.mouse_pan_motion)
	def mouse_pan_off(self,event):
		messaging.ignore("4",self.mouse_pan_motion)
	def mouse_pan_motion(self,event):
		x,y=event.pos
		dx,dy=x-self.pan_x,y-self.pan_y
		self.pan_x,self.pan_y=x,y
		self.center(self.center_x-dx*self.distance_x/self.width,self.center_y-dy*self.distance_y/self.height)
	def check_terrain_click(self,x,y):
		if x>self.x and y>self.y and x<self.x+self.width and y<self.y+self.height:
			x3,y3=self.screen_to_cam(x,y)
			x2,y2=self.cam_to_world(x3,y3)
			messaging.propagate("terrain_clicked",(x2,y2))
