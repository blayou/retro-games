#from doctest import NORMALIZE_WHITESPACE
#from tkinter.tix import CELL
#from token import TYPE_COMMENT
import pygame
import sys
import random
import pathlib
import time

#from requests import head

record = None
state = "END"
score_path = str(pathlib.Path(__file__).parent.absolute()) + "\\filessnake.py"
score_path = score_path.replace("\\",'/')

class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos



class Food:
    def __init__(self):
        x = random.randint(0, NB_COL - 1)
        y = random.randint(0, NB_COL - 1)
        self.block = Block(x, y)

    def draw_food(self):
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (72, 212, 98), rect)

class Snake:
    def __init__(self):
       self.body = [Block(2,6), Block(3,6), Block(4, 6)]
       self.direction = "RIGHT"
       self.score = 0

    def draw_snake(self):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            block_rect = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (83, 177, 253), block_rect)

    def move_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count - 1]

        if self.direction == "RIGHT":
            new_head = Block(old_head.x + 1, old_head.y)
            
        elif self.direction == "LEFT":
            new_head = Block(old_head.x - 1, old_head.y)
        
        elif self.direction == "TOP":
            new_head = Block(old_head.x, old_head.y - 1)

        else :
            new_head = Block(old_head.x, old_head.y + 1)

        self.body.append(new_head)
        
    def reset_snake(self):

        if self.score > record:
            file = open(score_path,"a")
            file.write("\nrecord = "+ str(self.score))
            file.close
            time.sleep(1)
            print("NOUVEAU RECORD :",self.score,"!")
        else :
            time.sleep(1)
            print("Score :",self.score)
        
        time.sleep(2)
        q = str(input("Appuyez sur entrée pour relancer la partie"))
        time.sleep(0.5)
        self.body = [Block(2,6), Block(3,6), Block(4, 6)]
        self.direction = "RIGHT"
        

    

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.generate_food()
        

    def update(self):
        self.snake.move_snake()
        self.check_head_on_food()
        self.game_over()

    def draw_game_element(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_head_on_food(self):
        snake_lenght = len(self.snake.body)
        snake_head_block = self.snake.body[snake_lenght - 1]
        food_block = self.food.block

        if snake_head_block.x == food_block.x and snake_head_block.y == food_block.y:
            self.generate_food()
            self.snake.score += 1
        else:
            self.snake.body.pop(0)

    def generate_food(self):
        self.food = Food()
        should_generate_food = True
        while should_generate_food:
            count = 0
            for block in self.snake.body:
                if block.x == self.food.block and block.y == self.food.block.y:
                    count += 1
            if count == 0:
                should_generate_food = False
            else:
                self.food = Food()
            
    def game_over(self):
        global state
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]
        if (snake_head.x not in range(0, NB_COL)) or (snake_head.y not in range(0, NB_ROW)):
            if self.snake.score > record:
                file = open(score_path,"w")
                file.write("\nrecord = "+ str(self.snake.score))
                file.close
                time.sleep(1)
                print("NOUVEAU RECORD :",self.snake.score,"!")
            else :
                time.sleep(1)
                print("Score :",self.snake.score)
            
            self.snake.score = 0
            self.snake.body = [Block(2,6), Block(3,6), Block(4, 6)]
            self.snake.direction = "RIGHT"
            state = "END"
            

        for block in self.snake.body[0:snake_length - 1]:
            if block.x == snake_head.x and block.y == snake_head.y:
                if self.snake.score > record:
                    file = open(score_path,"w")
                    file.write("\nrecord = "+ str(self.snake.score))
                    file.close
                    time.sleep(1)
                    print("NOUVEAU RECORD :",self.snake.score,"!")
                else :
                    time.sleep(1)
                    print("Score :",self.snake.score)
                self.snake.score = 0
                self.snake.body = [Block(2,6), Block(3,6), Block(4, 6)]
                self.snake.direction = "RIGHT"
                exec(open(score_path).read())
                state = "END"
                break

pygame.init()

NB_COL = 10
NB_ROW = 15
CELL_SIZE = 40

screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))

timer = pygame.time.Clock()

game_on = True

game = Game()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 400)

def showGrid():
    for i in range(0, NB_COL):
        for j in range(0, NB_ROW):
            grille = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (243, 243, 243), grille, width=1)


while game_on:
    if state == "END":
        exec(open(score_path).read())
        state = "ON"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == SCREEN_UPDATE:
            game.update()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_z or event.key == pygame.K_w:
                if game.snake.direction != "DOWN":
                    game.snake.direction = "TOP"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if game.snake.direction != "TOP":
                    game.snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT or event.key == pygame.K_q or event.key == pygame.K_a:
                if game.snake.direction != "RIGHT":
                    game.snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if game.snake.direction != "LEFT":
                    game.snake.direction = "RIGHT"

    
    screen.fill(pygame.Color('white'))
    showGrid()
    game.draw_game_element()
    pygame.display.update()
    timer.tick(60)