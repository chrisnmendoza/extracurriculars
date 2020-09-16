#!/usr/bin/python3

from sense_hat import SenseHat
import sys, pygame
import random
import os


#intialization
pygame.init()
pygame.display.init()
sense = SenseHat()
press = sense.stick.get_events()

# sets up window configuations
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Space Invader")
icono = pygame.image.load('icon.png')
pygame.display.set_icon(icono)

#player
playerIm = pygame.image.load('player.png')
playerX = 200
playerY = 330

def player():
	screen.blit(playerIm,(playerX,playerY))

#shooting thing
rocketIm = pygame.image.load('rocket.png')
rocketX = playerX
rocketY = playerY
shot=0

def rocket():
	screen.blit(rocketIm,(rocketX,rocketY))

def rocketReset():
        rocketY = playerY
        rocketX = playerX

#Enemies
enemyIm = pygame.image.load('invader.png')
enemyX = random.randint(0,400)
enemyY = 10
enemyMove = 0
def enemy():
	screen.blit(enemyIm,(enemyX,enemyY))

#explosion
explodeIm = pygame.image.load('explosion.png')
hitSpot = [enemyX,enemyY]
def explode():
    screen.blit(explodeIm,(hitSpot[0],hitSpot[1]))

#game action
running = True
changePos=0
changeScore=1
score=0
testingMode=1
testCounter=0
counter=0
explosionTimer=0
while running:
	screen.fill((0,0,0))
	for event in pygame.event.get():	#handles window
		if event.type == pygame.QUIT:
			running = False
		for event in sense.stick.get_events():
			if event.action == "pressed": #handles joystick usage
				if event.direction == "up":
					running = False
				else:
					if event.direction == "left":
						changePos=1
						playerX = playerX - 25
					elif event.direction == "right":
						playerX = playerX + 25
						changePos=1
					elif event.direction == "middle" and shot == 0:
						print("rocket shot!")
						rocketReset()
						rocketY=playerY
						rocketX=playerX+23
						shot=1
					if playerX > 400: #Handles wrapping around corners of screen
						playerX = 0
					elif playerX < 0:
						playerX = 400
	if changeScore == 1:
		sense.show_letter(str(score),[0,0,120])
		changeScore = 0
	player()
	if counter >= 500:
                if enemyMove == 1:
                    enemyX = enemyX - 10
                    if enemyX < 0:
                        enemyX = 400
                elif enemyMove == 2:
                    enemyX+=10
                    if enemyX > 400:
                        enemyX=0
                enemyY+=5
                counter=0
	enemy()
	if explosionTimer > 0:
            explode()
            explosionTimer+=1
            if explosionTimer>50:
                explosionTimer=0
	if shot==1: #handles rocket shooting
		rocketY = rocketY - 1
		rocket()
		if rocketX >= enemyX-10 and rocketX <= enemyX+35 and rocketY <= enemyY+10 and rocketY >= enemyY-35: #handles when rocket hits enemy
			print("enemy hit!")
			hitSpot[0]=enemyX
			hitSpot[1]=enemyY
			score+=1
			if score > 9:
                            score = 0
			changeScore=1
			shot=0
			explode()
			explosionTimer=1
			enemyX=random.randint(0,400)
			enemyY=random.randint(0,125)
			enemyMove=random.randint(0,2)
		if rocketY <=0:
			print("rocket done")
			shot=0
	if testingMode==1:	#handles test stuff
		if changePos == 1:
			print("New x position is: ",playerX)
			print("Rocket X position is: ",rocketX)
			print("Enemy position is: (",enemyX,",",enemyY,")\n")
			changePos=0
		if shot == 1:
			testCounter+=1
			if testCounter >=20:
				testCounter=0
				print("Rocket position is: (",rocketX,",",rocketY,")")
	counter+=1
	pygame.display.update() #Need this to update display

