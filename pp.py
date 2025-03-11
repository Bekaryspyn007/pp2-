import math
import pygame

pygame.init()

screen = pygame.display.set_mode((800,480)) #creating a fame window
# set mode() takes a tuple as an argument

running = True 
while running: #game loop
    for event in pygame.event.get(): #even loop
        if event.type == pygame.QUIT:
            running = False
