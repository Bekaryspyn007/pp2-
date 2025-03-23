import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Функция для генерации случайного места для еды
def random_food():
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    return x, y

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()
    
    def grow(self):
        self.body.append(self.body[-1])
    
    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:] or not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT):
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = random_food()
    running = True
    
    while running:
        screen.fill(BLACK)
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                    snake.direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                    snake.direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                    snake.direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                    snake.direction = (CELL_SIZE, 0)
        
        # Движение змейки
        snake.move()
        
        # Проверка на столкновение
        if snake.check_collision():
            running = False
        
        # Проверка поедания еды
        if snake.body[0] == food:
            snake.grow()
            food = random_food()
        
        # Отрисовка еды
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
        
        # Отрисовка змейки
        snake.draw()
        
        pygame.display.flip()
        clock.tick(8)
    
    pygame.quit()

if __name__ == "__main__":
    main()
