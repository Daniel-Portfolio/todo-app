from flask import Flask
from pymongo import MongoClient
from os import getenv
import logging

MONGO_URI = getenv("MONGO_URI")
SECRET_KEY = getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["MONGO_URI"] = MONGO_URI
app.logger.setLevel(logging.INFO)

client = MongoClient(app.config["MONGO_URI"])
db = client['todos']

from app import routes
