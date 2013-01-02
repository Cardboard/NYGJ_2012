####### TITLE OF GAME #########
####### by Cardboard ##########
## for the Ney Year Game Jam ##
####### 2012-13 ###############

import pygame, sys, random
from pygame.locals import *
#import the player and level
import player
import level

SCALE = 32 
WIDTH = 32 * 20 

class Game:
	def __init__(self, UPDATELIST=[]):
		pygame.init()
		self.surface = pygame.display.set_mode((WIDTH, 3*SCALE))
		pygame.display.set_caption("TITLE OF GAME by Cardboard")
		self.updateList = UPDATELIST
		self.surface.fill((255,255,255))
		self.delay = 100 # delay before spawning each new block
		self.stage = 1
		# choices for random block generation
		self.block_height = [1, 2]
		self.block_lane = [0, 1, 2]
		self.block_speed = [2, 3, 4, 5]
		self.block_color = [(255, 0, 61), (255, 204, 51), (204, 255, 51),
				(255, 51, 102), (245, 0, 61), (184, 0, 46), (255, 51, 204)]
	def draw(self):
		self.surface.fill((255,255,255))
		for drawFunc in updateList:
			drawFunc.draw(self.surface)
		pygame.display.update()
	def randomLevel(self, level):
		if pygame.time.get_ticks() % self.delay == 0:
			level.newBlock( random.choice(self.block_height),
				random.choice(self.block_lane),
				random.choice(self.block_speed),
				random.choice(self.block_color) )
	def changeDelay(self):
		ticks = pygame.time.get_ticks()
		if ticks > 150000 and self.stage == 2:
			self.delay = 10
			self.stage = 3
		if ticks > 50000 and self.stage == 1:
			self.delay =  50
			self.stage = 2

#MAIN PRE-LOOP
player = player.Player(SCALE)
level = level.Level(SCALE, WIDTH)
updateList = [player, level]
game = Game(updateList)

#MAIN LOOP
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			print('QUITTING...')
			pygame.quit()
			sys.exit()

	#KEYPRESSES
	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		print('QUITTING...')
		pygame.quit()
		sys.exit()
#PLAYER: CHANGE LANES
	if keys[pygame.K_UP]:
		player.move(0)		
	if keys[pygame.K_DOWN]:
		player.move(2)
	if (not keys[pygame.K_UP]) and (not keys[pygame.K_DOWN]):
		player.move(1)
#PLAYER: CHANGE X
	if keys[pygame.K_SPACE]:
		player.x = SCALE * 2
	if (not keys[pygame.K_SPACE]):
		player.x = 0	
#LEVEL RELATED
	game.changeDelay()
	game.randomLevel(level)
	level.move()
	level.collision(player)
	level.cleanup()
	if keys[pygame.K_RIGHT]:
		level.newBlock()
	if keys[pygame.K_LEFT]:
		level.newBlock(2, 1, 5, (128, 128, 0))
#DRAW EVERYTHING!
	game.draw()
