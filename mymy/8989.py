import pygame
import psycopg2
import random
import sys

# --- DATABASE SETUP ---
conn = psycopg2.connect(dbname="mybase", user="postgres", password="12345678", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1
    );
""")
conn.commit()

# --- DATABASE FUNCTIONS ---
def get_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    return cur.fetchone()

def create_user(username):
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
    conn.commit()
    return user_id

def get_user_score(user_id):
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    return cur.fetchone()

def update_user_score(user_id, score, level):
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
    conn.commit()

# --- GAME SETUP ---
pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Colors
WHITE, RED, GREEN, BLACK = (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction
speed = 10

# Food
food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

# Game state
score = 0
level = 1
pause = False

# --- USER LOGIN ---
username = input("Enter your username: ")
user = get_user(username)

if user:
    user_id = user[0]
    score, level = get_user_score(user_id)
    speed += level * 2
    print(f"Welcome back, {username}! Your level: {level}, score: {score}")
else:
    user_id = create_user(username)
    print(f"New user '{username}' created!")

# --- MAIN GAME LOOP ---
def game_over():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_user_score(user_id, score, level)
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            if event.key == pygame.K_DOWN: change_to = 'DOWN'
            if event.key == pygame.K_LEFT: change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: change_to = 'RIGHT'
            if event.key == pygame.K_p:
                pause = not pause
                if pause:
                    update_user_score(user_id, score, level)
                    print("Game paused and saved.")

    if pause:
        continue

    # Direction logic
    if change_to == 'UP' and not snake_direction == 'DOWN': snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP': snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT': snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT': snake_direction = 'RIGHT'

    # Move
    if snake_direction == 'UP': snake_pos[1] -= 10
    if snake_direction == 'DOWN': snake_pos[1] += 10
    if snake_direction == 'LEFT': snake_pos[0] -= 10
    if snake_direction == 'RIGHT': snake_pos[0] += 10

    # Snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        if score % 50 == 0:
            level += 1
            speed += 2
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    # Draw
    win.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    win.blit(score_text, [10, 10])

    pygame.display.update()

    # Check collision
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        update_user_score(user_id, score, level)
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            update_user_score(user_id, score, level)
            game_over()

    clock.tick(speed)
