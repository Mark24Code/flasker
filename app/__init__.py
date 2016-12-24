from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate, MigrateCommand

import settings

app = Flask(__name__)
app.config.from_object(settings)

## extension
db = SQLAlchemy(app)
migrate = Migrate(app, db)

toolbar = DebugToolbarExtension(app)
manager = Manager(app)

## manager helpers
manager.add_command('db', MigrateCommand)

## app self
from app import views, models

## custom app plugin
import blog
import sample

app.register_blueprint(blog.bp)
app.register_blueprint(sample.bp)
