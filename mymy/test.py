import pygame
pygame.init()

w,h =800,600

screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("My code")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,0,0))

pygame.quit()
