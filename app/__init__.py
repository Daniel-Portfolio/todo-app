from flask import Flask, request
from pymongo import MongoClient
from os import getenv
import logging

MONGO_URI = getenv("MONGO_URI")
SECRET_KEY = getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["MONGO_URI"] = MONGO_URI
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

client = MongoClient(app.config["MONGO_URI"])
db = client['todos']


@app.before_request
def log_request_info():
    app.logger.info('Request: %s %s %s', request.method,
                    request.path, request.data)


@app.after_request
def log_response_info(response):
    app.logger.info('Response: %s %s', response.status, response.data)
    return response


from app import routes
