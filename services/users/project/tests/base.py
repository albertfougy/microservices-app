from flask_testing import TestCase
from project import db

from project import create_app

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setup(self):
        db.create_all()
        db.session.commit()
    
    def teardown(self):
        db.session.remove()
        db.drop_all()