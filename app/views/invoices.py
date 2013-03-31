from flask import render_template, session, redirect, url_for, request, flash
from app import app, db
from app.models import Invoice, Client, Project

@app.route('/invoices')
def invoices():
	if session.get('username'):
		invoices = Invoice.query.order_by('name')
		return render_template('invoices/invoices.html',
			title = 'invoices',
			invoices = invoices)
	else:
		return redirect(url_for('login'))

@app.route('/invoices/<int:invoice_id>')
def view_invoice(invoice_id):
	if session.get('username'):
		invoice = Invoice.query.get(invoice_id)
		return render_template('invoices/view.html',
			title = invoice.name,
			invoice = invoice)
	else:
		return redirect(url_for('login'))

@app.route('/invoices/create', methods = ['GET', 'POST'])
def create_invoice():
	if session.get('username'):
		clients = Client.query.order_by('name')
		projects = Project.query.order_by('name')
		if request.method == 'POST':
			client = Client.query.get(request.form['client'])
			project = Project.query.get(request.form['project'])
			invoice = Invoice(
				name = request.form['name'],
				currency = request.form['currency'],
				status = request.form['status'],
#				sent_date = request.form['sent_date'],
#				due_date = request.form['due_date'],
#				total_price = request.form['total_price'],
				notes = request.form['notes'],
				payment = request.form['payment'],
				internal_notes = request.form['internal_notes'],
				client = client,
				project = project)
			db.session.add(invoice)
			db.session.commit()
			flash("Invoice '%s' was added." % invoice.name)
			return redirect(url_for('invoices'))
		return render_template('invoices/create.html',
			title = 'Add a New Invoice',
			clients = clients,
			projects = projects)
	else:
		return redirect(url_for('login'))

@app.route('/invoices/edit/<int:invoice_id>', methods = ['GET', 'POST'])
def edit_invoice(invoice_id):
	if session.get('username'):
		invoice = Invoice.query.get(invoice_id)
		clients = Client.query.order_by('name')
		projects = Project.query.order_by('name')
		if request.method == 'POST':
			client = Client.query.get(request.form['client'])
			project = Project.query.get(request.form['project'])
			invoice.name = request.form['name']
			invoice.currency = request.form['currency']
			invoice.status = request.form['status']
#			invoice.sent_date = request.form['sent_date']
#			invoice.due_date = request.form['due_date']
#			invoice.total_price = request.form['total_price']
			invoice.notes = request.form['notes']
			invoice.payment = request.form['payment']
			invoice.internal_notes = request.form['internal_notes']
			invoice.client = client
			invoice.project = project
			db.session.add(invoice)
			db.session.commit()
			flash("Invoice '%s' has been updated." % invoice.name)
			return redirect(url_for('invoices'))
		return render_template('invoices/edit.html',
			title = 'Edit Invoice %s' % invoice.name,
			invoice = invoice,
			clients = clients,
			projects = projects)
	else:
		return redirect(url_for('login'))

@app.route('/invoices/delete/<int:invoice_id>', methods = ['GET', 'POST'])
def delete_invoice(invoice_id):
	if session.get('username'):
		invoice = Invoice.query.get(invoice_id)
		if request.method == 'POST':
			db.session.delete(invoice)
			db.session.commit()
			flash("Invoice '%s' has been deleted." % invoice.name)
			return redirect(url_for('invoices'))
		return render_template('invoices/delete.html',
			title = 'Delete Invoice %s' % invoice.name,
			invoice = invoice)
	else:
		return redirect(url_for('login'))