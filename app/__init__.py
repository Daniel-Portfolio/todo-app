from flask import Flask
from flask_pymongo import PyMongo
from dotenv import dotenv_values

config = dotenv_values(".env.dev")
app = Flask(__name__)
app.config["SECRET_KEY"] = config["SECRET_KEY"]
app.config["MONGO_URI"] = f"mongodb://{config['MONGO_USER']
                                       }:{config['MONGO_PWD']}@127.0.0.1:27017/todo"


client = PyMongo(app)
db = client.db

from app import routes
