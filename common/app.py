from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@py.vansin.top/deepl?charset=utf8mb4'
db = SQLAlchemy(app)
