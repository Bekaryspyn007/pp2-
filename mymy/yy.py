import pygame

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шарик и Квадрат")

# Параметры объектов
circle_x, circle_y = 400, 300  # Начальная позиция шарика
circle_radius = 20  # Радиус шарика
circle_speed = 5  # Скорость шарика

square_x, square_y = 200, 200  # Начальная позиция квадрата
square_size = 40  # Размер квадрата
square_speed = 5  # Скорость квадрата

# Основной цикл игры
running = True
while running:
    pygame.time.delay(20)  # Задержка для стабильной скорости игры

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажали на крестик, выходим
            running = False

    keys = pygame.key.get_pressed()  # Получаем список нажатых клавиш

    # Движение шарика (стрелки)
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Движение квадрата (WASD)
    if keys[pygame.K_a]:
        square_x -= square_speed
    if keys[pygame.K_d]:
        square_x += square_speed
    if keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_s]:
        square_y += square_speed

    # Ограничения для шарика (чтобы не выходил за границы)
    circle_x = max(circle_radius, min(WIDTH - circle_radius, circle_x))
    circle_y = max(circle_radius, min(HEIGHT - circle_radius, circle_y))

    # Ограничения для квадрата (чтобы не выходил за границы)
    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Рисуем объекты
    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_radius)  # Синий шарик
    pygame.draw.rect(screen, (255, 0, 0), (square_x, square_y, square_size, square_size))  # Красный квадрат

    pygame.display.flip()  # Обновляем экран

pygame.quit()
