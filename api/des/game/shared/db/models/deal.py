from des.common.database import db

class Deal(db.Model):
    __tablename__ = "deal"
    id = db.Column(db.Integer(), primary_key=True)
    broker = db.Column(db.Integer(), db.ForeignKey('broker.id'), nullable=False)
    cartel = db.Column(db.Integer(), db.ForeignKey('cartel.id'), nullable=False)
    mafia = db.Column(db.Integer(), db.ForeignKey('mafia.id'), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Deal %r>' % self.id

class Payload(db.Model):
    __tablename__ = "payload"
    id = db.Column(db.Integer(), primary_key=True)
    deal = db.Column(db.Integer(), db.ForeignKey('deal.id'))
    cartel_cut = db.Column(db.Float(), nullable=False)
    broker_cut = db.Column(db.Float(), nullable=False)
    mafia_cut = db.Column(db.Float(), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    stage = db.Column(db.Integer(1), nullable=False)

