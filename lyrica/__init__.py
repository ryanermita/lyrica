from flask import Flask
from pymongo import MongoClient
# instantiate lyrica app
lyrica = Flask(__name__)
# instantiate database connection and db itself.
db_client = MongoClient('localhost', 27017)
db = db_client['python-backbone-sample-app-db']

# import app.py
from lyrica import app
