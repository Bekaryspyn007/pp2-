import pygame

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")


BACKGROUND_COLOR = (20, 20, 30)  
TEXT_COLOR = (0, 255, 170)  


font = pygame.font.Font(None, 72)
text = "Адик пидр айй"

image = pygame.image.load("photo_2025-03-13_03-27-20 (2).jpg") 
image = pygame.transform.scale(image, (300, 300))  


x = WIDTH
y = HEIGHT // 2 + 50 
speed = 5

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BACKGROUND_COLOR)  


    screen.blit(image, (x, y - 120))  


    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, (x, y))

    x -= speed  

    if x < -text_surface.get_width():  
        x = WIDTH  

    pygame.display.flip()  
    clock.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
