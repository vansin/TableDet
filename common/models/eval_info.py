# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from ..app import db

class EvalInfo(db.Model):
    __tablename__ = 'eval_info'

    id = db.Column(db.Integer, primary_key=True)
    epoch = db.Column(db.Integer)
    dataset = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    config = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    algorithm = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    checkpoint_size = db.Column(db.Float(asdecimal=True))
    iou = db.Column(db.Float(asdecimal=True))
    detail = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    ap = db.Column(db.Float(asdecimal=True))
    num_gts = db.Column(db.Integer)
    num_dets = db.Column(db.Integer)
    recall = db.Column(db.Float(asdecimal=True))
    precision = db.Column(db.Float(asdecimal=True))
    f1_score = db.Column(db.Float(asdecimal=True))
    recall_in_max_f1_score = db.Column(db.Float(asdecimal=True))
    precision_in_max_f1_score = db.Column(db.Float(asdecimal=True))
    max_f1_score = db.Column(db.Float(asdecimal=True))
