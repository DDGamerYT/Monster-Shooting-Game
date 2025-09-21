import pygame
import random
import math
import os

pygame.init()


screen = pygame.display.set_mode((1276, 652))

title = "Shooter Game"
icon = pygame.image.load('data/Game Logo.png')
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

bg = pygame.image.load('data/Background.jpg')

pygame.mixer.music.load('data/game music.mp3')
pygame.mixer.music.play(-1)


bullet_sound = pygame.mixer.Sound('data/Bullet Sound.wav')
Boss_explosion_sound = pygame.mixer.Sound('data/Boss Defeat explosion.wav')
explosion_sound = pygame.mixer.Sound('data/explosion.wav')

#player Data
player_img = pygame.image.load('data/plane.png')
player_x = 606
player_y = 550
playerx_change = 0

#enemy Data

num_of_enemies_2 = 1
enemy_x_2 = []
enemy_y_2 = []
enemyx_change_2 = []
enemyy_change_2 = []
enemy_img_3 = []

num_of_enemies_1 = 12
enemy_x_1 = []
enemy_y_1 = []
enemyx_change_1 = []
enemyy_change_1 = []
enemy_img_2 = []


num_of_enemies = 8
enemy_img_1 = []
enemy_x = []
enemy_y = []
enemyx_change = []
enemyy_change = []

for i in range(num_of_enemies):
	enemy_img_1.append(pygame.image.load('data/enemy.png'))
	enemy_x.append(random.randint(0, 1212))
	enemy_y.append(random.randint(20, 120))
	enemyx_change.append(0.8)
	enemyy_change.append(40)

for i in range(num_of_enemies_1):
	enemy_img_2.append(pygame.image.load('data/enemy 2.png'))
	enemy_x_1.append(random.randint(0, 1212))
	enemy_y_1.append(random.randint(20, 120))
	enemyx_change_1.append(3)
	enemyy_change_1.append(55)

for i in range(num_of_enemies_2):
	enemy_img_3.append(pygame.image.load('data/Boss Enemy.png'))
	enemy_x_2.append(random.randint(0, 1212))
	enemy_y_2.append(random.randint(20, 120))
	enemyx_change_2.append(6)
	enemyy_change_2.append(70)

#Bullet Data
bullet_img = pygame.image.load('data/bullet.png')
bullet_x = 0
bullet_y = 550
bullet_state = 'ready'
bullety_change = -4

score = 251
score_font = pygame.font.Font('data/Aldrich-Regular.ttf', 32)
score_x = 10
score_y = 10

game_over_img = pygame.image.load('data/game_over.jpg')
game_over_x = 310
game_over_y = 70

restart_font = pygame.font.Font('data/Aldrich-Regular.ttf', 32)
restart_x = 460
restart_y = 300

winner_font = pygame.font.Font('data/Aldrich-Regular.ttf', 150)

game_status = 'running'

high_score = 0
high_score_x = 950
high_score_y = 10

check = 'not win'
heart = 3

if os.path.exists('high_score.txt'):
    with open('high_score.txt', 'r') as f:
        high_score_data = f.read()
        if high_score_data:
            high_score = int(high_score_data)

def show_high_score(x, y):
	high_score_img = score_font.render(f"HIGH SCORE : {high_score}", True, (255, 255, 255))
	screen.blit(high_score_img, (x, y))

def show_toplayagain(x, y):
	tostart_img = restart_font.render("Press 'P' To TO_PLAY_AGAIN", True, (255, 255, 255))
	screen.blit(tostart_img, (x, y))

def show_restart(x, y):
	restart_img = restart_font.render("Press 'R' To RESTART", True, (255, 255, 255))
	screen.blit(restart_img, (x, y))


def show_game_over(x, y):
	global game_status
	screen.blit(game_over_img, (x, y))
	pygame.mixer.music.stop()
	game_status = 'end'


def show_score(x, y):
	score_img = score_font.render(f"SCORE : {score}", True, (255, 255, 255))
	screen.blit(score_img, (x, y))

def isCollistion(x1, y1, x2, y2, a):
	distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
	if a == 1:
		if distance <30:
			return True
		else:
			return False
	elif a == 2:
		if distance < 90:
			return True
		else :
			return False
	elif a == 3:
		if distance < 190:
			return True
		else :
			return False
def bullet(x, y):
	screen.blit(bullet_img, (x+16, y+10))

def enemy_1(x, y, i):
	screen.blit(enemy_img_1[i], (x, y))

def enemy_2(x, y, i):
	screen.blit(enemy_img_2[i], (x, y))

def enemy_3(x, y, i):
	screen.blit(enemy_img_3[i], (x, y))

def player(x, y):
	screen.blit(player_img, (x, y))

run = True
while run:
	screen.fill((255, 255, 255))
	screen.blit(bg, (0, 0))
	boundary_line = score_font.render("-----------------------------------------------------------------------------------------------------------------------------", True, (255, 255, 255))
	screen.blit(boundary_line, (0, 538))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_high_score = high_score
			with open('high_score.txt', 'w') as f:
				f.write(f"{save_high_score}")
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				playerx_change = 2.5
				if score >= 251 and score <= 500:
					playerx_change = 3.5
				elif score >= 501:
					playerx_change = 4
			if event.key == pygame.K_LEFT:
				playerx_change = -2.5
				if score >= 251 and score <= 500:
					playerx_change = -3
				elif score >= 501:
					playerx_change = -3.8
			if event.key == pygame.K_SPACE:
				if bullet_state == 'ready':
					bullet_state = 'fire'
					bullet_x = player_x
					bullet(bullet_x, bullet_y)
					bullet_sound.play()

			if event.key == pygame.K_r or pygame.K_p:
				if game_status == 'end':
					heart = 3
					game_status = 'running'
					score = 0
					player_x = 606
					pygame.mixer.music.play(-1)
					for i in range(num_of_enemies):
						enemy_x[i] = random.randint(0, 1212)
						enemy_y[i] = random.randint(20, 120)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				playerx_change = 0
			if event.key == pygame.K_LEFT:
				playerx_change = 0

	show_score(score_x, score_y)
	show_high_score(high_score_x, high_score_y)


	#Bullet
	if bullet_state == 'fire':
		if bullet_y<10:
			bullet_y=550
			bullet_state = 'ready'
		if score <= 50:
			bullety_change = -4
		if score >= 251 and score <= 500:
			bullety_change =-8 
		elif score >= 501:
			bullety_change =-12
		bullet_y += bullety_change
		bullet(bullet_x, bullet_y)


	#Enemy
	if score <= 50:
		for i in range(num_of_enemies):

			if enemy_y[i] > 502:
				for j in range(num_of_enemies):
					enemy_y[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x[i] += enemyx_change[i]

			if enemy_x[i] <= 0:
				enemy_x[i] = 0
				enemyx_change[i] = 0.8
				enemy_y[i] += enemyy_change[i]
			if enemy_x[i] >= 1212:
				enemy_x[i] = 1212
				enemyx_change[i] = -0.8
				enemy_y[i] += enemyy_change[i]
			enemy_1(enemy_x[i], enemy_y[i], i)


			#Collistion
			collistion = isCollistion(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 1)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x[i] = random.randint(0, 1212)
				enemy_y[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score
	elif score >= 51 and score <= 100:
		for i in range(num_of_enemies):
			if enemy_y[i] > 502:
				for j in range(num_of_enemies):
					enemy_y[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x[i] += enemyx_change[i]

			if enemy_x[i] <= 0:
				enemy_x[i] = 0
				enemyx_change[i] = 1.1
				enemy_y[i] += enemyy_change[i]
			if enemy_x[i] >= 1212:
				enemy_x[i] = 1212
				enemyx_change[i] = -1.1
				enemy_y[i] += enemyy_change[i]
			enemy_1(enemy_x[i], enemy_y[i], i)


			#Collistion
			collistion = isCollistion(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 1)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x[i] = random.randint(0, 1212)
				enemy_y[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score


	elif score >=101 and score <= 150:
		for i in range(num_of_enemies):
			if enemy_y[i] > 502:
				for j in range(num_of_enemies):
					enemy_y[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x[i] += enemyx_change[i]

			if enemy_x[i] <= 0:
				enemy_x[i] = 0
				enemyx_change[i] = 1.8
				enemy_y[i] += enemyy_change[i]
			if enemy_x[i] >= 1212:
				enemy_x[i] = 1212
				enemyx_change[i] = -1.8
				enemy_y[i] += enemyy_change[i]
			enemy_1(enemy_x[i], enemy_y[i], i)


			#Collistion
			collistion = isCollistion(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 1)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x[i] = random.randint(0, 1212)
				enemy_y[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score

	elif score >=151 and score <= 200:
		for i in range(num_of_enemies):
			if enemy_y[i] > 502:
				for j in range(num_of_enemies):
					enemy_y[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x[i] += enemyx_change[i]

			if enemy_x[i] <= 0:
				enemy_x[i] = 0
				enemyx_change[i] = 2
				enemy_y[i] += enemyy_change[i]
			if enemy_x[i] >= 1212:
				enemy_x[i] = 1212
				enemyx_change[i] = -2
				enemy_y[i] += enemyy_change[i]
			enemy_1(enemy_x[i], enemy_y[i], i)
			if score > high_score:
					high_score = score


			#Collistion
			collistion = isCollistion(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 1)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x[i] = random.randint(0, 1212)
				enemy_y[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()

	elif score >= 201 and score <= 250:
		for i in range(num_of_enemies):
			if enemy_y[i] > 502:
				for j in range(num_of_enemies):
					enemy_y[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x[i] += enemyx_change[i]

			if enemy_x[i] <= 0:
				enemy_x[i] = 0
				enemyx_change[i] = 3
				enemy_y[i] += enemyy_change[i]
			if enemy_x[i] >= 1212:
				enemy_x[i] = 1212
				enemyx_change[i] = -3
				enemy_y[i] += enemyy_change[i]
			enemy_1(enemy_x[i], enemy_y[i], i)
			if score > high_score:
					high_score = score


			#Collistion
			collistion = isCollistion(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 2)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x[i] = random.randint(0, 1212)
				enemy_y[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
	elif score >= 251 and score <= 300:
		for i in range(num_of_enemies_1):
			if enemy_y_1[i] > 425:
				for j in range(num_of_enemies_1):
					enemy_y_1[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x_1[i] += enemyx_change_1[i]

			if enemy_x_1[i] <= 0:
				enemy_x_1[i] = 0
				enemyx_change_1[i] = 3
				enemy_y_1[i] += enemyy_change_1[i]
			if enemy_x_1[i] >= 1212:
				enemy_x_1[i] = 1212
				enemyx_change_1[i] = -3
				enemy_y_1[i] += enemyy_change_1[i]
			enemy_2(enemy_x_1[i], enemy_y_1[i], i)


			#Collistion
			collistion = isCollistion(enemy_x_1[i], enemy_y_1[i], bullet_x, bullet_y, 2)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x_1[i] = random.randint(0, 1212)
				enemy_y_1[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score


	elif score >= 301 and score <= 360:
		for i in range(num_of_enemies_1):
			if enemy_y_1[i] > 425:
				for j in range(num_of_enemies_1):
					enemy_y_1[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x_1[i] += enemyx_change_1[i]

			if enemy_x_1[i] <= 0:
				enemy_x_1[i] = 0
				enemyx_change_1[i] = 4
				enemy_y_1[i] += enemyy_change_1[i]
			if enemy_x_1[i] >= 1212:
				enemy_x_1[i] = 1212
				enemyx_change_1[i] = -4
				enemy_y_1[i] += enemyy_change_1[i]
			enemy_2(enemy_x_1[i], enemy_y_1[i], i)


			#Collistion
			collistion = isCollistion(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 2)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x_1[i] = random.randint(0, 1212)
				enemy_y_1[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score

	elif score >= 361 and score <= 411:
		for i in range(num_of_enemies_1):
			if enemy_y_1[i] > 450:
				for j in range(num_of_enemies_1):
					enemy_y_1[j] = 1400
				show_game_over(game_over_x, game_over_y)
				show_restart(restart_x, restart_y)

			enemy_x_1[i] += enemyx_change_1[i]

			if enemy_x_1[i] <= 0:
				enemy_x_1[i] = 0
				enemyx_change_1[i] = 4
				enemy_y_1[i] += enemyy_change_1[i]
			if enemy_x_1[i] >= 1212:
				enemy_x_1[i] = 1212
				enemyx_change_1[i] = -4
				enemy_y_1[i] += enemyy_change_1[i]
			enemy_2(enemy_x_1[i], enemy_y_1[i], i)


			#Collistion
			collistion = isCollistion(enemy_x_1[i], enemy_y_1[i], bullet_x, bullet_y, 2)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				enemy_x_1[i] = random.randint(0, 1212)
				enemy_y_1[i] = random.randint(20, 120)
				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score


	elif score>= 501:
		if check == 'not win':
			for i in range(num_of_enemies_2):
				if enemy_y_2[i] > 270:
					for j in range(num_of_enemies_2):
						enemy_y_2[j] = 1400
					show_game_over(game_over_x, game_over_y)
					show_restart(restart_x, restart_y)

			enemy_x_2[i] += enemyx_change_2[i]

			if enemy_x_2[i] <= 0:
				enemy_x_2[i] = 0
				enemyx_change_2[i] = 4
				enemy_y_2[i] += enemyy_change_2[i]
			if enemy_x_2[i] >= 1212:
				enemy_x_2[i] = 1212
				enemyx_change_2[i] = -4
				enemy_y_2[i] += enemyy_change_2[i]
			enemy_3(enemy_x_2[i], enemy_y_2[i], i)


			#Collistion
			collistion = isCollistion(enemy_x_2[i], enemy_y_2[i], bullet_x, bullet_y, 3)
			if collistion:
				bullet_y = 550
				bullet_state = 'ready'
				heart = heart - 1
				if heart == 0:
					check = 'win'
					game_status = 'end'
					for j in range(num_of_enemies_2):
						enemy_y_2[j] = 1400

				score += 1
				explosion_sound.play()
				if score > high_score:
					high_score = score
	if heart == 0:
		winner_img = winner_font.render("WINNER", True, (0, 255, 0))
		screen.blit(winner_img, (315, 230))
		show_toplayagain(restart_x-60, restart_y-150)


	#player
	player_x += playerx_change

	if player_x <= 0:
		player_x = 0
	if player_x >= 1212:
		player_x = 1212


	player(player_x, player_y)


	pygame.display.update()

	
