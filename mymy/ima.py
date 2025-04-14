import pygame

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Image in Pygame")

# Load image
image = pygame.image.load("lab8/racer/Enemy.png")  # Replace with your image path
image = pygame.transform.scale(image, (100, 100))  # Resize if needed
x, y = 300, 200  # Initial position

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))  # Clear screen with a background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]:    y -= 5
    if keys[pygame.K_DOWN]:  y += 5

    # Draw image at new position
    screen.blit(image, (x, y))
    pygame.display.update()
    clock.tick(60)  # Limit FPS to 60

pygame.quit()
