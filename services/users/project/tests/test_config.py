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