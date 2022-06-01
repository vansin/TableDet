# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


from ..app import db


class TrainInfo(db.Model):
    __tablename__ = 'train_info'

    id = db.Column(db.Integer, primary_key=True)
    config = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    dataset = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    algorithm = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    epoch = db.Column(db.Integer)
    eval_epoch = db.Column(db.Integer)
    cmd = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
