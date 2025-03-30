import pygame

pygame.init()

w,h=800,600

radius = 50
speed = 2
cy,cx =300,400


screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("MYNE")

running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    keys = pygame.key.get_pressed()

    # Движение шарика (стрелки)
    if keys[pygame.K_LEFT]:
        cx -= speed
    if keys[pygame.K_RIGHT]:
        cx += speed
    if keys[pygame.K_UP]:
        cy -= speed
    if keys[pygame.K_DOWN]:
        cy += speed

    cx = max(radius, min(w - radius, cx))
    cy = max(radius, min(h - radius, cy))

    screen.fill((255,255,255))

    pygame.draw.circle(screen, (0, 0, 255), (cx, cy),radius) 

    pygame.display.flip() 

pygame.quit()
