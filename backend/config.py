from flask import Flask
# SQLAlchemy is a library that allows you to interact with a SQL database
from flask_sqlalchemy import SQLAlchemy
# Cross origin requests allows you to make a request to this backend from a different domain
from flask_cors import CORS

app = Flask(__name__)

# now we can send requests to this backend from a different domain
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)