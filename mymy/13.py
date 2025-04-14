import psycopg2

# Connect to your PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    dbname="mybase",
    user="postgres",
    password="12345678",
    port=5432
)

cur = connection.cursor()

# Create the table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100),
    grade INT
);
""")

# Sample data to insert
sample_data = [
    ('Abdulkarim', 'Bekarys', 95),
    ('Amina', 'Ali', 88),
    ('Nursultan', 'Pidr', 76),
    ('Kotakbas', 'Yeskali', 90)
]

# Insert data
for name, surname, grade in sample_data:
    cur.execute("INSERT INTO students (name, surname, grade) VALUES (%s, %s, %s)", (name, surname, grade))

# Commit changes and close connection
connection.commit()
cur.close()
connection.close()

print("Table created and data inserted successfully.")
