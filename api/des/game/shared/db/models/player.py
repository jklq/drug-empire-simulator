from des.common.database import db
from sqlalchemy.ext.declarative import declared_attr

class Player(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    @declared_attr
    def user(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=False)
    account_type = db.Column(db.String(1), nullable=True)

