import psycopg2

# Подключаемся к существующей базе данных
conn = psycopg2.connect(
    dbname="ьнифыу",      # Имя базы данных, которую ты создал в pgAdmin
    user="postgres",      # Имя пользователя
    password="12345678",      # Твой пароль от PostgreSQL
    host="localhost",     # Локальный сервер
    port="5432"           # Порт по умолчанию
)

cur = conn.cursor()

# 1. Создаём таблицу, если её нет
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
""")

# 2. Вставляем данные
cur.execute("""
    INSERT INTO users (name, email)
    VALUES
        ('Abdulkarim', 'karim@example.com'),
        ('Ali', 'ali@example.com'),
        ('Amina', 'amina@example.com')
    ON CONFLICT (email) DO NOTHING;
""")

# 3. Выводим содержимое таблицы
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()

print("Таблица users:")
for row in rows:
    print(row)

# Завершаем соединение
conn.commit()
cur.close()
conn.close()

