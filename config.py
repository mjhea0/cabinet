import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Deactivate DEBUG in a production system
DEBUG = True
CSRF = True
# Choose a hard to guess SECRET_KEY
SECRET_KEY = 'development'

# Login username/password
USERNAME = 'admin'
PASSWORD = 'pass'

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')