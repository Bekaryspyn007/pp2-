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
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Racer")

# Lanes
LANE_WIDTH = WIDTH // 4
lanes = [LANE_WIDTH * i + LANE_WIDTH // 2 - 25 for i in range(4)]  # Four lanes

# Player Car
car_width, car_height = 50, 100
car_x, car_y = lanes[1], HEIGHT - 150
car_speed = 7

# Enemy Cars
enemy_width, enemy_height = 50, 100
enemy_speed = 7
enemies = []

# Spawn multiple enemy cars
for _ in range(4):
    lane = random.choice(lanes)
    enemies.append([lane, random.randint(-400, -100)])

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)  # Background color (road)
    
    # Draw lanes
    for i in range(1, 4):
        pygame.draw.line(screen, YELLOW, (LANE_WIDTH * i, 0), (LANE_WIDTH * i, HEIGHT), 5)

    # Draw Player Car
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))  # Car Body
    pygame.draw.rect(screen, BLACK, (car_x + 5, car_y + 10, 10, 10))  # Left Headlight
    pygame.draw.rect(screen, BLACK, (car_x + 35, car_y + 10, 10, 10))  # Right Headlight

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get Key Presses (Lane Movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > lanes[0]:  
        car_x -= LANE_WIDTH  # Move left
    if keys[pygame.K_RIGHT] and car_x < lanes[3]:  
        car_x += LANE_WIDTH  # Move right

    # Move Enemy Cars
    for enemy in enemies:
        enemy[1] += enemy_speed  # Move enemy down
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))  # Enemy Car

        # Reset Enemy if off-screen
        if enemy[1] > HEIGHT:
            enemy[1] = random.randint(-400, -100)
            enemy[0] = random.choice(lanes)

        # Collision Detection
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)

        if car_rect.colliderect(enemy_rect):
            print("Crash! Game Over!")
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
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
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Racer")

# Lanes
LANE_WIDTH = WIDTH // 4
lanes = [LANE_WIDTH * i + LANE_WIDTH // 2 - 25 for i in range(4)]  # Four lanes

# Player Car
car_width, car_height = 50, 100
car_x, car_y = lanes[1], HEIGHT - 150
car_speed = 7

# Enemy Cars
enemy_width, enemy_height = 50, 100
enemy_speed = 7
enemies = []

# Spawn multiple enemy cars
for _ in range(4):
    lane = random.choice(lanes)
    enemies.append([lane, random.randint(-400, -100)])

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)  # Background color (road)
    
    # Draw lanes
    for i in range(1, 4):
        pygame.draw.line(screen, YELLOW, (LANE_WIDTH * i, 0), (LANE_WIDTH * i, HEIGHT), 5)

    # Draw Player Car
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))  # Car Body
    pygame.draw.rect(screen, BLACK, (car_x + 5, car_y + 10, 10, 10))  # Left Headlight
    pygame.draw.rect(screen, BLACK, (car_x + 35, car_y + 10, 10, 10))  # Right Headlight

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get Key Presses (Lane Movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > lanes[0]:  
        car_x -= LANE_WIDTH  # Move left
    if keys[pygame.K_RIGHT] and car_x < lanes[1]:  
        car_x += LANE_WIDTH  # Move right

    # Move Enemy Cars
    for enemy in enemies:
        enemy[1] += enemy_speed  # Move enemy down
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))  # Enemy Car

        # Reset Enemy if off-screen
        if enemy[1] > HEIGHT:
            enemy[1] = random.randint(-400, -100)
            enemy[0] = random.choice(lanes)

        # Collision Detection
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)

        if car_rect.colliderect(enemy_rect):
            print("Crash! Game Over!")
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
