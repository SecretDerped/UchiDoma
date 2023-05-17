import datetime
import random
import string

from . import db

SHORT_LEN = 6


def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=SHORT_LEN))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short


class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255))
    short = db.Column(db.String(SHORT_LEN), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
