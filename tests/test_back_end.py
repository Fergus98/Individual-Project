import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import *
from application.models import *

import os

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
                SQLALCHEMY_DATABASE_URI=str(os.getenv('SQL_URI')))
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        game1 = Game(game_no="12", losing_team="yankees", winning_team="Padres", score="16")


        # save users to database
        db.session.add(game1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
   
        
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('showGames'))
        self.assertEqual(response.status_code, 200)
        
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('showTeams'))
        self.assertEqual(response.status_code, 200)
        
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('showPlayers'))
        self.assertEqual(response.status_code, 200)
