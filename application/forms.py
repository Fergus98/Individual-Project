from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class GameForm(FlaskForm):
    game_no = StringField('Game Number',
        validators = [
            DataRequired(),
            Length(min=0, max=30)
        ]
    )
    losing_team = StringField('Losing Team',
        validators = [
            DataRequired(),
            Length(min=4, max=30)
        ]
    )
    winning_team = StringField('Winning Team',
        validators = [
            DataRequired(),
            Length(min=4, max=100)
        ]
    )
    score = IntegerField('Game Score',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField('Save the Game!')

class TeamForm(FlaskForm):
    team_id = IntegerField('Team Number',
        validators = [
            DataRequired()
        ]
    )
    
    wins = IntegerField('Number of Wins',
        validators = [
            DataRequired()
        ]
    )
    
    losses = IntegerField('Number of Losses',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField('Save the Team!')

class PlayerForm(FlaskForm):
    player_id = IntegerField('Player Number',
        validators = [
            DataRequired(),
        ]
    )
    team = StringField('Team',
        validators = [
            DataRequired(),
        ]
    )
    player_name = StringField('Player name',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit = SubmitField('Save the Player!')

class UpdateGame(FlaskForm):
    game_no = StringField('Game Number',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    losing_team = StringField('Losing Team',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    winning_team = StringField('Winning Team',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    score = StringField('Game Score',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Update the Game!')
