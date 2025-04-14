import pygame
import math
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
CLOCK_COLOR = (200, 180, 120)
HAND_COLOR = (50, 50, 50)
SECOND_HAND_COLOR = (255, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Old Clock")
clock = pygame.time.Clock()

def draw_clock():
    """Draw the clock face."""
    pygame.draw.circle(screen, CLOCK_COLOR, CENTER, RADIUS)
    pygame.draw.circle(screen, (0, 0, 0), CENTER, RADIUS, 5)  # Outer border
    pygame.draw.circle(screen, (0, 0, 0), CENTER, 5)  # Center dot

    # Draw hour markers
    for i in range(12):
        angle = math.radians(i * 30)
        outer_x = CENTER[0] + RADIUS * 0.9 * math.cos(angle)
        outer_y = CENTER[1] - RADIUS * 0.9 * math.sin(angle)
        inner_x = CENTER[0] + RADIUS * 0.75 * math.cos(angle)
        inner_y = CENTER[1] - RADIUS * 0.75 * math.sin(angle)
        pygame.draw.line(screen, (0, 0, 0), (outer_x, outer_y), (inner_x, inner_y), 3)

def draw_hand(length, angle, color, thickness=5):
    """Draws a clock hand."""
    end_x = CENTER[0] + length * math.cos(angle)
    end_y = CENTER[1] - length * math.sin(angle)
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), thickness)

def get_time_angles():
    """Get angles for hour, minute, and second hands based on real time."""
    t = time.localtime()
    second_angle = math.radians((t.tm_sec / 60) * 360 - 90)
    minute_angle = math.radians((t.tm_min / 60) * 360 - 90)
    hour_angle = math.radians(((t.tm_hour % 12) / 12) * 360 - 90 + (t.tm_min / 60) * 30)
    return hour_angle, minute_angle, second_angle

running = True
while running:
    screen.fill((255, 255, 255))
    draw_clock()
    
    hour_angle, minute_angle, second_angle = get_time_angles()
    draw_hand(RADIUS * 0.5, hour_angle, HAND_COLOR, 8)
    draw_hand(RADIUS * 0.7, minute_angle, HAND_COLOR, 5)
    draw_hand(RADIUS * 0.85, second_angle, SECOND_HAND_COLOR, 2)
    
    pygame.display.flip()
    clock.tick(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
