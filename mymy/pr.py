import pygame

pygame.init()

w, h = 800, 600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("moya")
speed = 3
x, y = w // 2, h // 2

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - 50 > 0:  # Движение влево
        x -= speed
    if keys[pygame.K_RIGHT] and x + 50 < w:  # Движение вправо
        x += speed
    if keys[pygame.K_UP] and y - 50 > 0:  # Движение вверх
        y -= speed
    if keys[pygame.K_DOWN] and y + 50 < h:  # Движение вниз
        y += speed



    screen.fill((255,255,255))
    pygame.draw.line(screen,('blue'),(x,y),(x+50,y), 5)
    pygame.display.update()

pygame.quit()