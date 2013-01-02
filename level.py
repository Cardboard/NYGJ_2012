import pygame

class Level:
	def __init__(self, scale, width):
		self.blocks = []
		self.scale = scale
		self.width = width
	# create a new block
	def newBlock(self, HEIGHT=1, LANE=0, SPEED=3, COLOR=(128,0,0)):
		new_block = Block(self.scale, self.width, HEIGHT, SPEED, LANE, COLOR)
		self.blocks.append(new_block)
	# move all blocks to the left
	def move(self):
		for block in self.blocks:
			block.x -= block.speed
	# draw all blocks
	def draw(self, surface):
		for block in self.blocks:
			pygame.draw.rect(surface, block.color, (block.x, block.y, self.scale, block.height))
	# remove blocks as they move off the screen
	def cleanup(self):
		for block in self.blocks:
			if block.x < (0 - self.scale):
				self.blocks.remove(block)
	# check for collision with player
	def collision(self, player):
		for block in self.blocks: # check each block for a collision
			if player.lane in block.lane:
				if block.x > player.x and block.x < (player.x + self.scale):
					self.blocks.remove(block)
					#END_GAME_AND_SHOW_SCORE!

class Block:
	def __init__(self, scale, width, height, speed, lane, color):
		self.x = width 
		self.y = lane * scale
		self.height = height * scale
		self.speed = speed
		self.lane = [lane]
		self.color = color
		for i in range(lane, height+lane-1):
			self.lane.append(i)
