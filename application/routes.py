# import render_template function from the flask module
from flask import render_template, redirect, url_for, request, flash
 # import the app object from the ./application/__init__.py
from application import app, db
from application.models import *
from application.forms import *
from sqlalchemy.exc import IntegrityError

 # define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    
    return render_template('home.html', title='Home')

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
        try:
            db.session.commit()
        except IntegrityError:
            flash("Already an entry, you have been returned to the homepage, try again!")
            db.session.rollback()
          

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('games.html', title='Add Game', form=form)

@app.route('/showgames', methods=['GET', 'POST'])
def showGames():
    gameData=Game.query.all()
    return render_template('showgames.html', title='Games', game=gameData)

@app.route('/showteams', methods=['GET', 'POST'])
def showTeams():
    teamData=Team.query.all()
    return render_template('showteams.html', title='Teams', team=teamData)

@app.route('/showplayers', methods=['GET','POST'])
def showPlayers():
    playerData=Players.query.all()
    return render_template('showplayers.html', title='Players', player=playerData)

@app.route('/teams', methods=['GET', 'POST'])
def createTeam():
    form = TeamForm()
    if form.validate_on_submit():
        teamData = Team(
            team_id = form.team_id.data,
            player_id = 1,
            wins = form.wins.data,
            losses = form.losses.data
        )

        db.session.add(teamData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('team.html', title='Teams', form=form)


@app.route('/players', methods=['GET', 'POST'])
def createPlayer():
    form = PlayerForm()
    if form.validate_on_submit():
        playerData = Players(
            player_id = form.player_id.data,
            team1 = form.team1.data,
            player_name = form.player_name.data
        )

        db.session.add(playerData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('players.html', title='Players', form=form)


@app.route("/game/update", methods=["POST"])
def update():
    newscore = request.form.get("newscore")
    oldscore = request.form.get("oldscore")
    score = Game.query.filter_by(score=oldscore).first()
    score.score = newscore
   
    db.session.commit()
    
    return redirect(url_for('showGames'))
   
@app.route("/team/update", methods=["POST"])
def updateTeam():
    newwins = request.form.get("newwins")
    oldwins = request.form.get("oldwins")
    wins = Team.query.filter_by(wins=oldwins).first()
    wins.wins = newwins
   
    db.session.commit()
    
    return redirect(url_for('showTeams'))

@app.route('/game/delete/<toDelete>')
def deleteGame(toDelete):
    game = Game.query.filter_by(game_no=toDelete).first()
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('showGames'))

@app.route('/team/delete/<teamDelete>')
def deleteTeam(teamDelete):
    team = Team.query.filter_by(team_id=teamDelete).first()
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('showTeams'))

@app.route('/player/delete/<playerDelete>')
def deletePlayer(playerDelete):
    player = Players.query.filter_by(player_id=playerDelete).first()
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('showPlayers'))
