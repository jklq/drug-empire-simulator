from ....common.database import db
from .models.broker import Broker
from .models.mafia import Mafia
from .models.cartel import Cartel

def list_brokers():
    print("BROKERS:")
    print(Broker.query.first())
