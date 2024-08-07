from pymongo import MongoClient
from . import env

client = MongoClient(env.LINK)

db = client.todo_db

collection_name = db["todo_collection"]