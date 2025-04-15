import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",  # or your database host
    port="5432"         # default PostgreSQL port
)

cur = conn.cursor()

# SQL statement as a string
cur.execute("""
    CREATE TABLE cars (
        brand VARCHAR(25),
        year INT
    );
""")

conn.commit()
cur.close()
conn.close()
