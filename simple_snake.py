# Making Snake

import pygame
import time
import random

pygame.init()
#setup display - define dimensions of the game window

#screen dimensions
width = 800
height = 800

#create screen object
screen = pygame.display.set_mode((width,height))

#title
pygame.display.set_caption('Snake')
#set colors using RGB values
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# Set Game Loop and Event Handling
#initial variables

#initializing clock, setting size of snake and speed
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 20

#fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
#drawing snake

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])
#display score

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])
#function to display messages on screen

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
#main game loop

def gameLoop():
    game_over = False
    game_close = False

    #initial position of the snake's head
    x1 = width / 2
    y1 = height / 2

    #change in position (initially zero)
    x1_change = 0
    y1_change = 0

    #start with 1 block as the snake's length
    snake_List = []
    Length_of_snake = 1

    #generate initial position for the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    #initial snake speed
    snake_speed = 15

    #main game loop
    while not game_over:

        #loop for when the game is over but waiting for player input to quit or restart
        while game_close:
            screen.fill(blue)
            message("you lost! press q-quit or c-play again", red)
            pygame.display.update()

            #event handling loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True  #quit game
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  #restart game

        #event handling loop for game play
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True  #quit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #check if snake hits the boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        #update snake's head position
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

        #update snake's body
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        #check if snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #draw the snake and update the score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        #check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

            #increase snake speed every 10 points
            if (Length_of_snake - 1) % 10 == 0:
                snake_speed += 3

        #control the speed of the snake
        clock.tick(snake_speed)

    #quit the game
    pygame.quit()
    quit()

gameLoop()
