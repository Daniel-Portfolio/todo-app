from flask import Flask
from pymongo import MongoClient
from os import getenv
from secrets import token_urlsafe

MONGO_URI = getenv("MONGO_URI")

app = Flask(__name__)
app.config["SECRET_KEY"] = token_urlsafe(16)
app.config["MONGO_URI"] = MONGO_URI

client = MongoClient(app.config["MONGO_URI"])
db = client['todos']

from app import routes
