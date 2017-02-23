#!/usr/bin/env python
import os
import click
from flask_migrate import Migrate

from app import create_app, db
from app.config import APP_MODULE_NAME
from app.libs.util import import_all_models

# Flask App Instance
app = create_app(os.environ['FLASK_CONFIG'])

# import all models
import_all_models(APP_MODULE_NAME)

# migrate
migrate = Migrate(app, db)


# Flask CLI
@app.cli.command()
def create_db():
    """Init Database Tables."""
    click.echo("Create Tables Model:")
    resp = input('>[Warning] This will drop all databases! Are you sure? [Y/N]')
    if resp in ['y', 'Y', 'yes', 'YES']:
        print('dropping databases……')
        db.drop_all()
        print('drop finished.')
        print('init database tables ……')
        db.create_all()
        print('init success. :D')

    elif resp in ['n', 'N', 'no', 'No']:
        pass
    else:
        print('Input Errors! Please try again.')


@app.cli.command()
def init_db():
    """Init Database."""
    click.echo("Init Database Model:")
    resp = input('>[Warning] This will drop all databases! Are you sure? [Y/N]')
    if resp in ['y', 'Y', 'yes', 'YES']:
        print('dropping databases……')
        db.drop_all()
        print('drop finished.')
        print('init database ……')
        db.create_all()
        print('init success. :D')

    elif resp in ['n', 'N', 'no', 'No']:
        pass
    else:
        print('Input Errors! Please try again.')


@app.cli.command()
def drop_all():
    """Drop all database."""
    click.echo('Drop Databases Model:')
    resp = input('>[Warning] This will drop all databases! Are you sure? [Y/N]')
    if resp in ['y', 'Y', 'yes', 'YES']:
        print('dropping……')
        db.drop_all()
        print('drop finished. :D')
    elif resp in ['N','No','NO']:
        pass
    else:
        print('Input Errors! Please try again.')


@app.cli.command()
def test():
    """Test all unit test."""
    import unittest
    tests = unittest.TestLoader().discover('.', pattern='tests.py')
    unittest.TextTestRunner(verbosity=2).run(tests)


