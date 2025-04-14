import pygame
import math

# Init
pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ayazhan Drawing Heart ❤️")
clock = pygame.time.Clock()

# Colors and font
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
font = pygame.font.SysFont("Georgia", 32, bold=True)

# Load image (Put the image file path or link here)
image_path = "path_to_your_image.jpg"  # Укажи путь к изображению
image = pygame.image.load(image_path)
image_rect = image.get_rect(center=(width // 2, height // 2))  # Позиционируем картинку в центре

# Generate heart path
scale = 15
center_x, center_y = width // 2, height // 2
heart_path = []

for t in range(0, 3600):  # finer resolution
    rad = math.radians(t / 10)
    x = 16 * math.sin(rad) ** 3
    y = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
    x *= scale
    y *= -scale
    heart_path.append((center_x + x, center_y + y))

# Text setup
text = "Ayazhan"
text_surface = font.render(text, True, RED)

# For trail tracking
trail_points = set()
index = 0
stopped = False

running = True
while running:
    screen.fill(WHITE)

    # Draw trail
    for pos in trail_points:
        pygame.draw.circle(screen, DARK_RED, (int(pos[0]), int(pos[1])), 2)

    if not stopped:
        # Move along path
        p1 = heart_path[index % len(heart_path)]
        p2 = heart_path[(index + 1) % len(heart_path)]

        # Direction
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        angle = math.degrees(math.atan2(-dy, dx))

        # Rotate and draw word
        rotated_text = pygame.transform.rotate(text_surface, angle)
        rect = rotated_text.get_rect(center=p1)
        screen.blit(rotated_text, rect)

        # Add to trail
        trail_points.add(p1)

        # Stop when full heart drawn
        if len(trail_points) >= len(heart_path) - 5:  # small margin
            stopped = True

        # Progress
        index = (index + 2) % len(heart_path)

    # Draw image in the center
    screen.blit(image, image_rect)

    pygame.display.flip()
    clock.tick(60)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
