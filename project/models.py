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
    twitter_handle = db.Column(db.String(255))
    skype = db.Column(db.String(255))
    street = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    country = db.Column(db.String(255))
    notes = db.Column(db.Text(1000))
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Client {0}>'.format(self.last_name)


class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    description = db.Column(db.Text(1000))
    status = db.Column(db.String(255))
    project_start = db.Column(db.DateTime)
    project_end = db.Column(db.DateTime)
    hourly_rate = db.Column(db.Integer)
    quote = db.Column(db.Integer)
    notes = db.Column(db.Text(1000))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship(
        'Client', backref=db.backref('projects', lazy='dynamic'))

    def __repr__(self):
        return '<Project {0}>'.format(self.name)


class Invoice(db.Model):

    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    currency = db.Column(db.String(255))
    status = db.Column(db.String(255))
    sent_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    total_price = db.Column(db.Integer)
    notes = db.Column(db.Text(1000))
    payment = db.Column(db.Text(1000))
    internal_notes = db.Column(db.Text(1000))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship(
        'Client', backref=db.backref('invoices', lazy='dynamic'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship(
        'Project', backref=db.backref('invoices', lazy='dynamic'))

    def __repr__(self):
        return '<Invoice {0}>'.format(self.name)


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(255), index=True, nullable=False)
    task_status = db.Column(db.String(255))
    task_hours = db.Column(db.Float)
    task_price = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship(
        'Project', backref=db.backref('tasks', lazy='dynamic'))

    def __repr__(self):
        return '<Task {0}>'.format(self.name)


class Service(db.Model):

    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_name = db.Column(db.String(255), index=True, nullable=False)
    service_hours = db.Column(db.Float)
    service_price = db.Column(db.Float)
    hourly_rate = db.Column(db.Integer)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'))
    invoice = db.relationship(
        'Invoice', backref=db.backref('invoices', lazy='dynamic'))

    def __repr__(self):
        return '<Service {0}>'.format(self.name)
