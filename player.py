import pygame

class Player:
	def __init__(self, SCALE=1):
		self.scale = SCALE
		self.x = 0
		self.y = 1 * SCALE #can be 0,1,2
		self.width = (1 * SCALE)
		self.height = (1 + SCALE)
		self.color = (64,64,64)
		self.lane = 1
		# set player's starting health
		self.health = 3
		# self.jump is true when jumping or returning after a jump
		self.jumping = False
		
	def move(self, lane):
		if lane >= 0 and lane <= 2:
			self.y = lane * self.scale
			self.lane = lane	

	def jump(self):
		if self.x <= 0 and self.jumping == True:
			self.jumping = False
		elif self.x != 0 and self.jumping == True:
			self.x -= 4
	
	def reset(self):
		self.y = 1 * self.scale
	
	# called if the player collides with a block
	def hurt(self):
		self.health -= 1

	def checkHealth(self):
		if self.health == 3:
			self.color = (64,64,64)
		if self.health == 2:
			self.color = (128,128,128)
		if self.health == 1:
			self.color = (194,194,194)
		if self.health == 0:
			self.color = (255,255,255)

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
