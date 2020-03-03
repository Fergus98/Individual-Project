from application import db
from application.models import Game, Team

db.drop_all()
db.create_all()
