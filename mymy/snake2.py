import pygame
import psycopg2
import sys

# === PostgreSQL Setup ===
conn = psycopg2.connect(
    dbname="mybase",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def setup_db():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            level INTEGER,
            score INTEGER
        );
    ''')
    conn.commit()

def get_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    return cur.fetchone()

def create_user(username):
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    conn.commit()
    return cur.fetchone()[0]

def save_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()

def get_latest_score(user_id):
    cur.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    return cur.fetchone()

# === Game Setup ===
pygame.init()
setup_db()

username = input("Enter your username: ")
user = get_user(username)
if user:
    user_id = user[0]
    last_state = get_latest_score(user_id)
    if last_state:
        print(f"Welcome back, {username}! Last level: {last_state[0]} | Score: {last_state[1]}")
    else:
        print(f"Welcome back, {username}! No previous score found.")
else:
    user_id = create_user(username)
    print(f"New user created: {username}")

# === Game Configuration ===
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with DB")
clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50]]
snake_speed = 10
direction = "RIGHT"
change_to = direction
score = 0
level = 1
paused = False

def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

def game_over():
    save_score(user_id, level, score)
    pygame.quit()
    sys.exit()

# === Game Loop ===
while True:
    clock.tick(snake_speed + level)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game Paused. Saving...")
                    save_score(user_id, level, score)

    if paused:
        continue

    # Change direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if len(snake_body) > 1:
        snake_body.pop()

    # Check for collision with walls
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH or snake_pos[1] < 0 or snake_pos[1] > HEIGHT:
        game_over()

    # Update score and level
    score += 1
    if score % 50 == 0:
        level += 1

    # Draw everything
    win.fill((0, 0, 0))
    draw_snake(snake_body)
    pygame.display.update()
