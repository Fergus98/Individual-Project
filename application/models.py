from application import db

class Game(db.Model):
    game_no = db.Column(db.Integer, primary_key=True)
    losing_team = db.Column(db.String(30), nullable=False)
    winning_team = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Game Number: ', self.game_no,'\r\n',
            'Winning Team', self.winning_team, '\r\n','Losing Team: ', self.losing_team, '\r\n', self.score
            ])

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join([
            'Team Number: ', self.team_id,'\r\n',
            'Total Wins: ', self.wins, '\r\n', 'Losses: ', self.losses
            ])

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(30), nullable=False)
    player_name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Player ID: ', self.player_id,'\r\n',
            'Team: ', self.team, '\r\n', 'Player Name: ', self.player_name
            ])
