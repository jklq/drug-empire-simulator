from des.common.database import db
from .player import Player

class Cartel(Player):
    __tablename__ = "cartel"
    __table_args__ = {'extend_existing': True} 

    def __repr__(self):
        return '<Cartel %r>' % self.id
