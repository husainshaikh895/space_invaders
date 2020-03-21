'''Space invaders in turtle module(python3) '''
__author__ = 'https://GitHub.com/HusainShaikh895'

import turtle
import os
import time
import math
import random

# screen
window = turtle.Screen()
window.title('Space Invaders')
window.setup(550,600)
window.bgpic('bg.gif')
window.tracer(0)

turtle.register_shape('spaceship.gif')
# player
player = turtle.Turtle()
player.goto(-150, -250)
player.speed(0)
player.shape('spaceship.gif')
player.setheading(90)
player.penup()

dx = 15

# bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 3
bulletstate = 'ready'
# ready or fired



score = 0
# instructions pen
spen = turtle.Turtle()
spen.penup()
spen.hideturtle()
spen.color('red')
spen.speed(0)
spen.setposition(-200, 250)
spen.write(f'Score: {score}', align = 'center', font = ('ComicSans', 22, 'bold'))
os.system('afplay gameOver.mp3&')


# enemies
num_of_enemies = 5
enemies = []

# add enemies to the list
for i in range(num_of_enemies):
	enemies.append(turtle.Turtle())

turtle.register_shape('alien1.gif')
turtle.register_shape('alien2.gif')
turtle.register_shape('alien3.gif')
turtle.register_shape('alien4.gif')
turtle.register_shape('alien5.gif')

aliens = ['alien2.gif', 'alien3.gif', 'alien1.gif', 'alien4.gif', 'alien5.gif']

for enemy in enemies:
	enemy.penup()
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.shape(aliens[random.randint(0,4)])
	enemy.speed(0)
	enemy.setposition(x, y)
	enemy.speed = 2


# functions
def move_left():
	x = player.xcor()
	x -= dx
	if x < -250:
		return
	player.setx(x)

def move_right():
	x = player.xcor()
	x += dx
	if x > 250:
		return
	player.setx(x)

def fire_bullet():
	# usign already declared bulletstate variable in the global scope
	global bulletstate
	if bulletstate == 'ready':
		os.system('afplay bullet.mp3&')
		bulletstate = 'fired'
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow( t1.xcor() - t2.xcor(), 2) + math.pow( t1.ycor() - t2.ycor(), 2))
	if distance < 18:
		os.system('afplay explode.mp3&')
		return True
	else:
		return False


# keyboard binding
turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(fire_bullet, 'space')


# main loop
try:
	while(True):
		window.update()
		for enemy in enemies:
			x = enemy.xcor()
			if(x > 250 or x < -250):
				enemy.speed *= -1
				enemy.sety(enemy.ycor()-20)
			x += enemy.speed
			enemy.setx(x)

			# bullet move
			if bulletstate == 'fired':
				bullet.sety(bullet.ycor() + bulletspeed)
				# bullet collision
				if(isCollision(bullet, enemy)):
					score += 1
					bullet.hideturtle()
					bulletstate = 'ready'
					bullet.setposition(-350,-350)
					spen.clear()
					spen.write(f'Score: {score}', align = 'center', font=('ComicSans', 22, 'bold'))
					# reset the enemy
					enemy.setposition(-200,250)

			#enemy touches spaceship
			if(isCollision(enemy, player)):
				os.system('afplay gameOver.mp3&')
				spen.clear()
				spen.goto(0,0)
				spen.write(f'Game Over!!!\n   Score : {score}', align = 'center', font=('ComicSans', 30, 'bold'))
				time.sleep(2)
				quit()
		if(bullet.ycor() > 290):
			bullet.hideturtle()
			bulletstate = 'ready'
except:
	pass
























