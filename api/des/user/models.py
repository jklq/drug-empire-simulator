from ..common.database import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(35), unique=False, nullable=False)
    role = db.Column(db.String(1), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
