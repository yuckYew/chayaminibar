from app import db
from datetime import datetime

class User(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(64), index=True, unique=True)
    email           = db.Column(db.String(120), index=True, unique=True)
    firebase_uid    = db.Column(db.String(64), index=True, unique=True)
    rank_id         = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Rank(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64), index=True, unique=True)

class Admin(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class ChashTrade(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    timestamp   = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    price       = db.Column(db.Integer)
    quantity    = db.Column(db.Integer)

class Product(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(64), index=True, unique=True)
    timestamp   = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    price       = db.Column(db.Integer, index=True)
    barcode     = db.Column(db.Integer, index=True)

class ProductTrade(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    timestamp       = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name            = db.Column(db.String(64), index=True, unique=True)
    user            = db.Column(db.Integer, db.ForeignKey('user.id'))
    price           = db.Column(db.Integer, db.ForeignKey('product.price'))
    chash_trade_id  = db.Column(db.Integer, db.ForeignKey('chash_trade.id'))
