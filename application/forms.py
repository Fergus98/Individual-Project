from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class GameForm(FlaskForm):
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
    submit = SubmitField('Save the Game!')

class PlayersForm(FlaskForm):
    team_id = IntegerField('Team Number',
        validators = [
            DataRequired(),
            Length(min=1, max=200)
        ]
    )
    
    wins = IntegerField('Number of Wins',
        validators = [
            DataRequired(),
            Length(min=0, max=200)
        ]
    )
    
    losses = IntegerField('Number of Losses',
        validators = [
            DataRequired(),
            Length(min=0, max=200)
        ]
    )
class DeleteGame(FlaskForm):
    game_num = IntegerField('Number to delete', validators =[DataRequired()])
    submit = SubmitField('Delete')
