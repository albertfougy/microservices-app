# services/users/project/__init__.py


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
  

# instantiate the db
db = SQLAlchemy()  


def create_app(script_info=None):

    app=Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return{'app': app, 'db': db}

    return app



# import sys
# print(app.config, file=sys.stderr)

# Want to test, to ensure the proper config was loaded?

# Add a print statement to __init__.py, right before the route handler, 
# to view the app config to ensure that it is working:
