# import render_template function from the flask module
from flask import render_template
 # import the app object from the ./application/__init__.py
from application import app
from application.models import Game
 # define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    gameData = Game.query.first()
    return render_template('home.html', title='Home', game=gameData)
