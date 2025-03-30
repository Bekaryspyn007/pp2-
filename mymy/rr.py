import pygame

# Инициализация Pygame
pygame.init()

# Параметры окна
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Шарик")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Параметры шарика
cx, cy = w // 2, h // 2  # Начальная позиция в центре
radius = 20  # Радиус
speed = 5  # Скорость

# Шрифт
font = pygame.font.Font(None, 50)

# Флаг для экрана меню
menu = True

def draw_button(text, x, y, width, height):
    """Функция для рисования кнопки"""
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    label = font.render(text, True, BLACK)
    screen.blit(label, (x + 20, y + 10))

# Основной цикл
running = True
while running:
    screen.fill(WHITE)

    if menu:
        # Главное меню
        title = font.render("Шарик", True, BLACK)
        screen.blit(title, (w // 2 - 50, 100))

        # Кнопка "Играть"
        button_x, button_y, button_w, button_h = w // 2 - 75, 250, 150, 50
        draw_button("Играть", button_x, button_y, button_w, button_h)

        # Проверка клика на кнопку
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_w and button_y <= mouse_y <= button_y + button_h:
                    menu = False  # Переход в игру

    else:
        # Игровой процесс
        pygame.time.delay(20)

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

        # Ограничения для шарика
        cx = max(radius, min(w - radius, cx))
        cy = max(radius, min(h - radius, cy))

        # Очистка экрана и рисование шарика
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (cx, cy), radius)

    pygame.display.flip()

pygame.quit()
