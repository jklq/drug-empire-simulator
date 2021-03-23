from des.common.database import db
from .player import Player

class Broker(Player):
    __tablename__ = "broker"
    __table_args__ = {'extend_existing': True} 

    def __repr__(self):
        return '<Broker %r>' % self.id

class Vessel(db.Model):
    __tablename__ = "vessel"
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.Integer(), db.ForeignKey('broker.id'))
    fuel_efficiency = db.Column(db.Integer())
    speed = db.Column(db.Integer())
    detection_rate = db.Column(db.Integer())
    trips = db.Column(db.Integer())
    mileage = db.Column(db.Integer())
    profits = db.Column(db.Integer())
