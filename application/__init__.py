from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = 'jnnononibinoun5165ibijbIJBIBIJBIB'

db = SQLAlchemy(app)

from application import routes