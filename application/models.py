from application import db

class Game(db.Model):
    game_no = db.Column(db.Integer, primary_key=True)
    losing_team = db.Column(db.String(30), nullable=False)
    winning_team = db.Column(db.String(30), nullable=False)
    score = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Game Number: ', self.game_no,'\r\n',
            'Winning Team', self.winning_team, '\r\n','Losing Team: ', self.losing_team, '\r\n', self.score
            ])
