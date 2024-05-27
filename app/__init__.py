from flask import Flask
from pymongo import MongoClient
from dotenv import dotenv_values

cfg = dotenv_values(".env.dev")

app = Flask(__name__)
app.config["SECRET_KEY"] = cfg["SECRET_KEY"]
app.config["MONGO_URI"] = f"mongodb://{cfg['MONGO_USER']}" \
    f":{cfg['MONGO_PWD']}@127.0.0.1:27017/"

print(app.config["MONGO_URI"])

client = MongoClient(app.config["MONGO_URI"])
db = client[cfg["MONGO_DB"]]

from app import routes
