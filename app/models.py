from app import db

class Client(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), index = True)
	company = db.Column(db.String(255))
	website = db.Column(db.String(255))
	twitter = db.Column(db.String(255))
	email = db.Column(db.String(255))
	telephone = db.Column(db.String(255))
	skype = db.Column(db.String(255))
	street = db.Column(db.String(255))
	street_2 = db.Column(db.String(255))
	city = db.Column(db.String(255))
	state = db.Column(db.String(255))
	postcode = db.Column(db.String(255))
	country = db.Column(db.String(255))
	notes = db.Column(db.Text(1000))

	def __repr__(self):
		return '<Client %r>' % (self.name)

class Project(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), index = True)
	description = db.Column(db.Text(1000))
	status = db.Column(db.String(255))
	project_start = db.Column(db.DateTime)
	project_end = db.Column(db.DateTime)
	hourly_rate = db.Column(db.Integer)
	quote = db.Column(db.Integer)
	notes = db.Column(db.Text(1000))
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	client = db.relationship('Client', backref = db.backref('projects', lazy='dynamic'))

	def __repr__(self):
		return '<Project %r>' % (self.name)

class Invoice(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), index = True)
	currency = db.Column(db.String(255))
	status = db.Column(db.String(255))
	sent_date = db.Column(db.DateTime)
	due_date = db.Column(db.DateTime)
	total_price = db.Column(db.Integer)
	notes = db.Column(db.Text(1000))
	payment = db.Column(db.Text(1000))
	internal_notes = db.Column(db.Text(1000))
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	client = db.relationship('Client', backref = db.backref('invoices', lazy='dynamic'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	project = db.relationship('Project', backref = db.backref('invoices', lazy='dynamic'))

	def __repr__(self):
		return '<Invoice %r>' % (self.name)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	task_name = db.Column(db.String(255), index = True)
	task_status = db.Column(db.String(255))
	task_hours = db.Column(db.Float)
	task_price = db.Column(db.Integer)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	project = db.relationship('Project', backref = db.backref('tasks', lazy='dynamic'))

	def __repr__(self):
		return '<Task %r>' % (self.name)

class Service(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	service_name = db.Column(db.String(255), index = True)
	service_hours = db.Column(db.Float)
	service_price = db.Column(db.Float)
	hourly_rate = db.Column(db.Integer)
	invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
	invoice = db.relationship('Invoice', backref = db.backref('invoices', lazy='dynamic'))

	def __repr__(self):
		return '<Service %r>' % (self.name)