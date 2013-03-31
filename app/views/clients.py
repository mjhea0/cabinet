from flask import render_template, session, redirect, url_for, request, flash
from app import app, db
from app.models import Client

@app.route('/clients')
def clients():
	if session.get('username'):
		clients = Client.query.order_by('name')
		return render_template('clients/clients.html',
			title = 'Clients',
			clients = clients)
	else:
		return redirect(url_for('login'))

@app.route('/clients/<int:client_id>')
def view_client(client_id):
	if session.get('username'):
		client = Client.query.get(client_id)
		projects = client.projects.all()
		invoices = client.invoices.all()
		return render_template('clients/view.html',
			title = client.name,
			client = client,
			projects = projects,
			invoices = invoices)
	else:
		return redirect(url_for('login'))

@app.route('/clients/create', methods = ['GET', 'POST'])
def create_client():
	if session.get('username'):
		if request.method == 'POST':
			client = Client(
				name = request.form['name'],
				company = request.form['company'],
				website = request.form['website'],
				twitter = request.form['twitter'],
				email = request.form['email'],
				telephone = request.form['telephone'],
				skype = request.form['skype'],
				street = request.form['street'],
				street_2 = request.form['street_2'],
				city = request.form['city'],
				state = request.form['state'],
				postcode = request.form['postcode'],
				country = request.form['country'],
				notes = request.form['notes'])
			db.session.add(client)
			db.session.commit()
			flash("Client '%s' was added." % client.name)
			return redirect(url_for('clients'))
		return render_template('clients/create.html',
			title = 'Add a New Client')
	else:
		return redirect(url_for('login'))

@app.route('/clients/edit/<int:client_id>', methods = ['GET', 'POST'])
def edit_client(client_id):
	if session.get('username'):
		client = Client.query.get(client_id)
		if request.method == 'POST':
			client.name = request.form['name']
			client.company = request.form['company']
			client.website = request.form['website']
			client.twitter = request.form['twitter']
			client.email = request.form['email']
			client.telephone = request.form['telephone']
			client.skype = request.form['skype']
			client.street = request.form['street']
			client.street_2 = request.form['street_2']
			client.city = request.form['city']
			client.state = request.form['state']
			client.postcode = request.form['postcode']
			client.country = request.form['country']
			client.notes = request.form['notes']
			db.session.add(client)
			db.session.commit()
			flash("Client '%s' has been updated." % client.name)
			return redirect(url_for('clients'))
		return render_template('clients/edit.html',
			title = 'Edit %s' % client.name,
			client = client)
	else:
		return redirect(url_for('login'))

@app.route('/clients/delete/<int:client_id>', methods = ['GET', 'POST'])
def delete_client(client_id):
	if session.get('username'):
		client = Client.query.get(client_id)
		if request.method == 'POST':
			db.session.delete(client)
			db.session.commit()
			flash("Client '%s' has been deleted." % client.name)
			return redirect(url_for('clients'))
		return render_template('clients/delete.html',
			title = 'Delete %s' % client.name,
			client = client)
	else:
		return redirect(url_for('login'))