# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv() # to allow .env to work

# creditial info that gets pulled from .env. 
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

# labeling the connection uri. It pulls the credentials that are labeled
# above and plugs them into the uri
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

# labeling the client
client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

# making the database and showing it works
db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

# creating a collection
collection = db.pokemon_collection
print("---------------")
print("COLECTION:", type(collection), collection)

# show all the collections created to this point; print their title
print("--------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": "30",
    "exp": "760000000",
    "hp": "400",
    "metadata": {
        "a": "something",
        "b": "something else",
    }
})  # can insert nested structures / documents!!!
