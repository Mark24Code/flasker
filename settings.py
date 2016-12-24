import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#Form CSRF
CSRF_ENABLED = True
SECRET_KEY = "You can't find me"

#DATABASE
DATABASENAME = 'db.sqlite'
MIGRATIONNAME = 'migrations'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASENAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, MIGRATIONNAME)
