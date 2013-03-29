from app import db

class Client(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), index = True)
	company = db.Column(db.String(255))
	website = db.Column(db.String(255))
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
	name = db.Column(db.String(64), index = True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	client = db.relationship('Client', backref = db.backref('projects', lazy='dynamic'))

	def __repr__(self):
		return '<Project %r>' % (self.name)

class Invoice(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	client = db.relationship('Client', backref = db.backref('invoices', lazy='dynamic'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	project = db.relationship('Project', backref = db.backref('invoices', lazy='dynamic'))

	def __repr__(self):
		return '<Invoice %r>' % (self.name)