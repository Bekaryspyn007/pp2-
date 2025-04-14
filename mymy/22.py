import psycopg2
from tabulate import tabulate

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="mybase",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Создание таблицы (если ещё не создана)
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

# Вставка данных (игнорирует дубликаты по email)
cur.execute("""
INSERT INTO users (name, email)
VALUES
    ('Abdulkarim', 'karim@example.com'),
    ('Ali', 'ali@example.com'),
    ('Amina', 'amina@example.com')
ON CONFLICT (email) DO NOTHING
""")

# Получение данных
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

# Красивый вывод
print("\n📋 Таблица users:\n")
print(tabulate(rows, headers=["ID", "Name", "Email"], tablefmt="grid"))

# Завершение
conn.commit()
cur.close()
conn.close()

