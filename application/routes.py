# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
 # import the app object from the ./application/__init__.py
from application import app, db
from application.models import *
from application.forms import *
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
        db.session.commit()

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
            team = form.team.data,
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
    newgame = request.form.get("newgame")
    oldgame = request.form.get("oldgame")
    game = Game.query.filter_by(game_no=oldgame).first()
    game.game_no = newgame
    
    newlose = request.form.get("newlose")
    oldlose = request.form.get("oldlose")
    lose = Game.query.filter_by(losing_team=oldlose).first()
    lose.losing_team = newlose
    
    #newgame = request.form.get("newgame")
    #oldgame = request.form.get("oldgame")
    #game = Game.query.filter_by(game_no=oldgame).first()
    #game.game_no = newgame
    
    #newgame = request.form.get("newgame")
    #oldgame = request.form.get("oldgame")
    #game = Game.query.filter_by(game_no=oldgame).first()
    #game.game_no = newgame
    db.session.commit()
    
    return redirect(url_for('showGames'))

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
