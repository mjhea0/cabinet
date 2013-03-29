from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.views import dashboard
from app.views import clients
from app.views import projects
from app.views import invoices