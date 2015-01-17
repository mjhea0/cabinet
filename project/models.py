# project/models.py


import datetime

from project import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User {0}>'.format(self.email)


class Client(db.Model):

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), index=True, nullable=False)
    last_name = db.Column(db.String(255), index=True, nullable=False)
    email = db.Column(db.String(255))
    company = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    street = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    country = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Client {0}>'.format(self.last_name)


class Invoice(db.Model):

    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_number = db.Column(db.Integer)
    paid = db.Column(db.Boolean, nullable=False)
    invoice_date = db.Column(db.DateTime)
    sent_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    total_price = db.Column(db.Float, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship(
        'Client', backref=db.backref('invoices', lazy='dynamic'))

    def __repr__(self):
        return '<Invoice {0}>'.format(self.id)
