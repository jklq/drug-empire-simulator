from des.common.database import db
from .player import Player

class Mafia(Player):
    __tablename__ = "mafia"
    __table_args__ = {'extend_existing': True} 

    def __repr__(self):
        return '<Mafia %r>' % self.id
