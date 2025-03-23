import pygame

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Двигающийся текст")

# Настройки текста
font = pygame.font.Font(None, 72)
text = "Адик пидр Ибонын жынына тиме"
color = (255, 255, 255)  # Белый цвет

# Начальная позиция текста
x = WIDTH
y = HEIGHT // 2  # По центру экрана

# Скорость движения
speed = 5

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 0, 0))  # Черный фон

    # Рисуем текст
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

    # Двигаем текст влево
    x -= speed

    # Если текст вышел за экран, возвращаем его направо
    if x < -text_surface.get_width():
        x = WIDTH

    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
