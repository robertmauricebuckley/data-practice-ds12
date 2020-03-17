import psycopg2
import os
import json
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv() # look in the .env file for env vars and add them to env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

# Table Creation
query = """
CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""
cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", len(result))

# Data Insertion

# Approach 2
my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }
# insertion_query = "INSERT INTO test_table (name, data) VALUES (%s, %s)"
# cursor.execute(insertion_query,
#     ('A Rowwww', 'null')
# )
# cursor.execute(insertion_query,
#     ('Another row with JSONNNNN', json.dumps(my_dict))
# )

# Approach 3
insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
execute_values(cursor, insertion_query, [
 ('A rowwwww', 'null'),
 ('Another row, with JSONNNNN', json.dumps(my_dict)),
 ('Third row', "3")
])

cursor.execute("SELECT * FROM test_table;")
result = cursor.fetchall()
print("RESULT:", len(result))

connection.commit()