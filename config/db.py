from pymongo import MongoClient
from decouple import config

connection = MongoClient(config("MONGO_URI"))
