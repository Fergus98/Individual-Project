# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
 # import the app object from the ./application/__init__.py
from application import app, db
from application.models import Game
from application.forms import *
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
            losing_team = form.losing_team.data,
            winning_team = form.winning_team.data,
            score = form.score.data
        )

        db.session.add(gameData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('games.html', title='Add Game', form=form)

@app.route('/showgames', methods=['GET', 'POST'])
def showGames():
    gameData=Game.query.all()
    return render_template('showgames.html', title='Games', game=gameData)
    

@app.route('/teams', methods=['GET', 'POST'])
def createTeam():
    form = TeamForm()
    if form.validate_on_submit():
        teamData = Team(
            team_id = form.team_id.data,
            wins = form.wins.data,
            losses = form.losses.data
        )

        db.session.add(teamData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('team.html', title='Teams', form=form)

@app.route('/game/delete/<toDelete>')
def deleteGame(toDelete):
    game = Game.query.filter_by(game_no=toDelete).first()
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('showGames'))

