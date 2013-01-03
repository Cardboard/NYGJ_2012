########## blocks #############
####### by Cardboard ##########
## for the New Year Game Jam ##
######### 2012-13 #############

import pygame, sys, random
import pygame._view
from pygame.locals import *
#import the player and level
import player
import level

SCALE = 64
WIDTH = SCALE * 20 

class Game:
	def __init__(self, font, UPDATELIST=[]):
		pygame.init()
		self.surface = pygame.display.set_mode((WIDTH, 3*SCALE))
		pygame.display.set_caption("blocks by Cardboard")
		self.updateList = UPDATELIST
		self.surface.fill((255,255,255))
		self.delay = 1000 # delay before spawning each new block
		self.delay_end = 0
		self.stage = 1
		# choices for random block generation
		self.block_height = [1, 2]
		self.block_lane = [0, 1, 2]
		self.block_speed = [2, 3, 4, 5]
		self.block_color = [(255, 0, 61), (255, 204, 51), (204, 255, 51),
				(255, 51, 102), (245, 0, 61), (184, 0, 46), (255, 51, 204)]
		self.font = font
		self.score = 0
		self.startTime = pygame.time.get_ticks()
	def draw(self):
		self.surface.fill((255,255,255))
		for drawFunc in updateList:
			drawFunc.draw(self.surface)
		# PRINT THE SCORE
		self.surface.blit((self.font.render(str(round(self.score)).split('.')[0], 1, (100,100,100))), (1,1)) 
		pygame.display.update()
	def randomLevel(self, level):
		# IF A BLOCK WAS JUST MADE, START THE TIMER TO MAKE A NEW BLOCK
		if self.delay_end == 0:
			self.delay_end = self.ticks + self.delay
		# IF THE DELAY IS UP, MAKE A BLOCK
		if self.delay_end < self.ticks:
			level.newBlock( random.choice(self.block_height),
				random.choice(self.block_lane),
				random.choice(self.block_speed),
				random.choice(self.block_color) )
			self.delay_end = 0
	def changeDelay(self):
		self.ticks = pygame.time.get_ticks()
		if self.ticks > (100000 + self.startTime) and self.stage == 2:
			self.delay = 300
			# give the player a score bonus
			self.score += 500
			self.stage = 3
			print('STAGE 3')
		if self.ticks > (50000 + self.startTime) and self.stage == 1:
			self.delay =  500
			# give the player a score bonus
			self.score += 100
			self.stage = 2
			print('STAGE 2')
	def reset(self):
		self.delay = 1000
		self.delay_end = 0
		self.startTime = pygame.time.get_ticks()
		self.stage = 1
		self.score = 0
		player.health = 3

#MAIN PRE-LOOP
player = player.Player(SCALE)
level = level.Level(SCALE, WIDTH)
updateList = [player, level]
pygame.font.init()
font = pygame.font.Font(None, SCALE)
game = Game(font, updateList)
clock = pygame.time.Clock()
startTime = pygame.time.get_ticks()


running = True
#MAIN LOOP
while True:
	keys = pygame.key.get_pressed()
	# WHILE PLAYING THE GAME
	if running == True:
		#KEYPRESSES
		#PLAYER: CHANGE LANES
		if keys[pygame.K_UP]:
			player.move(0)		
		if keys[pygame.K_DOWN]:
			player.move(2)
		if (not keys[pygame.K_UP]) and (not keys[pygame.K_DOWN]):
			player.move(1)
		#PLAYER: CHANGE X
		if keys[pygame.K_SPACE]:
			player.jumping = True
			player.x = SCALE * 2
	
		#PLAYER: OTHER
		player.jump()
		player.checkHealth()
		#LEVEL RELATED
		game.changeDelay()
		game.randomLevel(level)
		level.move()
		level.collision(player)
		level.cleanup()
		if player.health == 0:
			running = False
		#DRAW EVERYTHING!
		game.draw()
		#TICK THE CLOCK!
		clock.tick(60)
		#ADD TO SCORE
		game.score += 0.1
		#RESTART THE GAME
		if keys[pygame.K_r]:
			game.reset()
	# WHILE AT THE ENDGAME SCREEN
	if running == False:
		scoreText = ('final score: %s' % str(round(game.score)).split('.')[0])
		endText = font.render(scoreText + '    play again? (spacebar)', 1, (100,100,100))
		game.surface.blit(endText, (SCALE, SCALE))
		pygame.display.update()
		if keys[pygame.K_r]:
			game.reset()
			running = True

	for event in pygame.event.get():
		if event.type == QUIT:
			print('QUITTING...')
			pygame.quit()
			sys.exit()	
	if keys[pygame.K_ESCAPE]:
		print('QUITTING...')
		pygame.quit()
		sys.exit()
