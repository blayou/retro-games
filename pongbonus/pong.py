import pygame
import sys
from random import randint
import time

pygame.init()
tailleFenetre = 810
screen = pygame.display.set_mode((tailleFenetre, tailleFenetre))
pong_1 = pygame.Rect(20, 360, 20, 100)
pong_2 = pygame.Rect(tailleFenetre - 20, 360, 20, 100)

class Ball:
    def __init__(self):
        self.x = 360
        self.y = 360
        self.vitesse_x = randint(2,6)
        self.vitesse_y = randint(2,6)

        if randint(1,2) == 1:
            self.direction_x = "LEFT"
        else :
            self.direction_x = "RIGHT"
        if randint(1,2) == 1:
            self.direction_y = "UP"
        else:
            self.direction_y = "DOWN"
        
    def move(self):

        if self.direction_y == "UP":
            self.y -= self.vitesse_y
        elif self.direction_y == "DOWN":
            self.y += self.vitesse_y
        if self.direction_x == "LEFT":
            self.x -= self.vitesse_x
        elif self.direction_x == "RIGHT":
            self.x += self.vitesse_x
    


timer = pygame.time.Clock()

x= 150
y = 200

ball = Ball()
score_1 = 0
score_2 = 0
state = None

game_on = True
direction_1 = None
direction_2 = None
while game_on:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.type == pygame.K_w:
                direction_1 = "UP"
            if event.key == pygame.K_s:
                direction_1 = "DOWN"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_z or event.key == pygame.K_s:
                direction_1 = None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                direction_2 = "UP"
            if event.key == pygame.K_k:
                direction_2 = "DOWN"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_i or event.key == pygame.K_k:
                direction_2 = None

    screen.fill((255, 255, 255))

    rayonBalle = 20
    pygame.draw.rect(screen, pygame.Color("black"), pong_1 )
    pygame.draw.rect(screen, pygame.Color("black"), pong_2 )
    pygame.draw.circle(screen, pygame.Color("black"), (ball.x, ball.y), rayonBalle)

    if direction_1 == "UP" and pong_1.top > 0:
        pong_1.top -= 10
    elif direction_1 == "DOWN" and pong_1.bottom < tailleFenetre:
        pong_1.bottom += 10
    if direction_2 == "UP" and pong_2.top > 0:
        pong_2.top -= 10
    elif direction_2 == "DOWN" and pong_2.bottom < tailleFenetre:
        pong_2.bottom += 10

    if ball.x - rayonBalle <= 0:
        #ball.direction_x = "RIGHT"
        #ball.vitesse_x = randint(ball.vitesse_x - 1, ball.vitesse_x + 1)
        score_2 += 1
        print("\nPlayer 2 scored !\nPlayer 1 //",score_1,"-",score_2,"// Player 2")
        state = "SCORED"
        time.sleep(1)

    elif ball.x + rayonBalle >= tailleFenetre:
        #ball.direction_x = "LEFT"
        #ball.vitesse_x = randint(ball.vitesse_x - 1,  ball.vitesse_x + 1)
        score_1 += 1
        print("\nPlayer 1 scored !\nPlayer 1 //",score_1,"-",score_2,"// Player 2")
        state = "SCORED"
        time.sleep(1)

    if ball.y - rayonBalle <= 0:
        ball.direction_y = "DOWN"
        ball.vitesse_y = randint(ball.vitesse_y - 1, ball.vitesse_y + 1)

    elif ball.y + rayonBalle >= tailleFenetre:
        ball.direction_y = "UP"
        ball.vitesse_y = randint(ball.vitesse_y - 1, ball.vitesse_y + 1)

    if ball.x - rayonBalle <= pong_1.right:
        if ball.y - rayonBalle >= pong_1.top and ball.y + rayonBalle <= pong_1.bottom:
            ball.direction_x = "RIGHT"
            if direction_1 != None:
                ball.direction_y = direction_1
    if ball.x + rayonBalle >= pong_2.left:
        if ball.y - rayonBalle >= pong_2.top and ball.y + rayonBalle <= pong_2.bottom:
            ball.direction_x = "LEFT"
            if direction_2 != None:
                ball.direction_y = direction_2




    if state == "SCORED":
        if score_1 >= 5 or score_2 >= 5:
            if score_1 < score_2:
                print("Player 2 wins !")
                print("Tapez entrée pour fermer")
                q = str(input(""))
                pygame.quit()
                sys.exit()
            else :
                print("Player 1 wins !")
                print("Tapez entrée pour fermer")
                q = str(input(""))
                pygame.quit()
                sys.exit()
        else :
            pong_1.bottom = ( tailleFenetre / 2 ) + 50
            pong_2.bottom = ( tailleFenetre / 2 ) + 50
            time.sleep(1)
            ball.__init__()
            state = "PLAYING"
        

    if ball.vitesse_x < 2 :
        ball.vitesse_x = 2
    if ball.vitesse_x > 6 :
        ball.vitesse_x = 6
    if ball.vitesse_y < 2 :
        ball.vitesse_y = 2
    if ball.vitesse_y > 6 :
        ball.vitesse_y = 6

    ball.move()
    pygame.display.update()
    timer.tick(60)