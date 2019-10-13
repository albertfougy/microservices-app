# services/users/project/tests/test_config.py

import os
import unittest
from flask import current_app
from flask_testing import TestCase
from project import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious' )
        self.assertFalse(app.config is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 
            os.get.environ('DATABASE_URL')
            )