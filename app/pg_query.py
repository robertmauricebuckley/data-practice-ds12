import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env vars and add them to env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

cursor.execute('SELECT * from test_table;')

result = cursor.fetchone()
print("RESULT:", result)