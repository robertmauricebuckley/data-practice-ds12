# app/pg_titanic.py
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

# making the connection with host of the database (ElephantSQL)
# takes the credential info from above that gets pulled from the .env
# and plugs it into the psycopg2 connect fuction.
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

# shows cursor is working
cursor = connection.cursor()
print("CURSOR:", cursor)

# GOAL: load the data/titanic.csv file into a PG database table!
# CREATE THE TABLE
# discern which columns (pandas?)
# columns are created by looking at the csv file and typing this out.
query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived int,
  pclass int,
  name varchar,
  sex varchar,
  age int,
  sib_spouse_count int,
  parent_child_count int,
  fare float8
);
"""
cursor.execute(query)


cursor.execute("SELECT * from passengers;")
result = cursor.fetchall()
print("PASSENGERS:", len(result))

if len(result) == 0:
    # INSERT RECORDS

    # creating a file path for the csv file that can be read correctly 
    # regardless of which directory you are in when you run it.
    # os.path.dirname(__file__) is saying "whats the directory where this file # is" that takes us to that folder then each next space is directions
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data","titanic.csv")
    print("FILE EXISTS?", os.path.isfile(CSV_FILEPATH))
    df = pandas.read_csv(CSV_FILEPATH)
    print(df.head())

    # turning the csv dataframe into a list of tuples; tuples are needed to be # able to insert them into the new table that was created
    rows = list(df.itertuples(index=False, name=None))

    # now creat a query that inserts data into the table
    insertion_query = "INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
    execute_values(cursor, insertion_query, rows)

# this saves the transaction
connection.commit()

    



