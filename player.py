import pygame

class Player:
	def __init__(self, SCALE=1):
		self.scale = SCALE
		self.x = 0
		self.y = 1 * SCALE #can be 0,1,2
		self.width = (1 * SCALE)
		self.height = (1 + SCALE)
		self.color = (0, 255, 0) #GREEN
		self.lane = 1
		
	def move(self, lane):
		if lane >= 0 and lane <= 2:
			self.y = lane * self.scale
			self.lane = lane	
	
	def reset(self):
		self.y = 1 * self.scale
	
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
