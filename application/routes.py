# import render_template function from the flask module
from flask import render_template, redirect, url_for
 # import the app object from the ./application/__init__.py
from application import app, db
from application.models import Game
from application.forms import GameForm
 # define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    gameData = Game.query.first()
    return render_template('home.html', title='Home', game=gameData)

@app.route('/game', methods=['GET', 'POST'])
def createGame():
    form = GameForm()
    if form.validate_on_submit():
        gameData = Game(
            game_no = form.game_no.data,
            winning_team = form.winning_team.data,
            losing_team = form.losing_team.data,
            score = form.score.data
        )

        db.session.add(gameData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('game.html', title='Add Game', form=form)
