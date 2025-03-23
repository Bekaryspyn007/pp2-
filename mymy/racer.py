import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Racer")

# Player Car (made of rectangles)
car_width, car_height = 50, 100
car_x, car_y = WIDTH // 2 - car_width // 2, HEIGHT - 150
car_speed = 5

# Obstacles
obstacle_width, obstacle_height = 50, 100
obstacle_x = random.randint(50, WIDTH - 100)
obstacle_y = -100
obstacle_speed = 7

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Background color

    # Draw Pixel Car
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))  # Car Body
    pygame.draw.rect(screen, BLACK, (car_x + 5, car_y + 10, 10, 10))  # Left Headlight
    pygame.draw.rect(screen, BLACK, (car_x + 35, car_y + 10, 10, 10))  # Right Headlight

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 50:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 100:
        car_x += car_speed

    # Move Obstacles
    obstacle_y += obstacle_speed
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))  # Obstacle

    # Reset Obstacles if off-screen
    if obstacle_y > HEIGHT:
        obstacle_y = -100
        obstacle_x = random.randint(50, WIDTH - 100)

    # Collision Detection
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if car_rect.colliderect(obstacle_rect):
        print("Crash! Game Over!")
        running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
