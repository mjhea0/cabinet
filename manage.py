# manage.py


import os
import unittest
import coverage
import datetime

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from project import app, db
from project.models import User, Client, Invoice


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(
        branch=True,
        include='project/*',
        omit="*/__init__.py"
    )
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print 'Coverage Summary:'
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    cov.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    cov.erase()


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email='ad@min.com', password='admin', admin=True))
    db.session.commit()


@manager.command
def create_data():
    """Creates sample data."""
    client = Client(
        first_name='Michael',
        last_name='Herman',
        email='michael@realpython.com',
        company='Real Python',
        website='https://realpython.com',
        telephone='415XXXXXX',
        street='210 3rd Ave #1',
        city='San Francisco',
        state='CA',
        postal_code='94122',
        country='United States',
        date_created=datetime.datetime.now()
    )
    db.session.add(client)
    client = Client.query.first()
    invoice = Invoice(
        paid=0,
        invoice_number=99,
        invoice_date=datetime.datetime.now(),
        due_date=datetime.datetime.now(),
        total_price=22.00,
        client=client
    )
    db.session.add(invoice)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
