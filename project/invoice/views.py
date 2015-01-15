# project/invoice/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask.ext.login import login_required

from project import db
from project.models import Invoice, Client, Project


################
#### config ####
################

invoice_blueprint = Blueprint('invoice', __name__,)


################
#### routes ####
################


@invoice_blueprint.route('/invoices')
@login_required
def invoices():
    invoices = Invoice.query.order_by('name')
    return render_template('invoices/invoices.html', invoices=invoices)


@invoice_blueprint.route('/invoices/<int:invoice_id>')
@login_required
def view_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    return render_template(
        'invoices/view.html',
        title=invoice.name,
        invoice=invoice
    )


@invoice_blueprint.route('/invoices/create', methods=['GET', 'POST'])
@login_required
def create_invoice():
    clients = Client.query.order_by('name')
    projects = Project.query.order_by('name')
    if request.method == 'POST':
        client = Client.query.get(request.form['client'])
        project = Project.query.get(request.form['project'])
        invoice = Invoice(
            name=request.form['name'],
            currency=request.form['currency'],
            status=request.form['status'],
            notes=request.form['notes'],
            payment=request.form['payment'],
            internal_notes=request.form['internal_notes'],
            client=client,
            project=project)
        db.session.add(invoice)
        db.session.commit()
        flash("Invoice '{0}' was added.".format(invoice.name))
        return redirect(url_for('invoice.invoices'))
    return render_template(
        'invoices/create.html',
        title='Add a New Invoice',
        clients=clients,
        projects=projects
    )


@invoice_blueprint.route(
    '/invoices/edit/<int:invoice_id>', methods=['GET', 'POST'])
@login_required
def edit_invoice(invoice_id):
        invoice = Invoice.query.get(invoice_id)
        clients = Client.query.order_by('name')
        projects = Project.query.order_by('name')
        if request.method == 'POST':
            client = Client.query.get(request.form['client'])
            project = Project.query.get(request.form['project'])
            invoice.name = request.form['name']
            invoice.currency = request.form['currency']
            invoice.status = request.form['status']
            invoice.notes = request.form['notes']
            invoice.payment = request.form['payment']
            invoice.internal_notes = request.form['internal_notes']
            invoice.client = client
            invoice.project = project
            db.session.add(invoice)
            db.session.commit()
            flash("Invoice '{0}' has been updated.".format(invoice.name))
            return redirect(url_for('invoice.invoices'))
        return render_template(
            'invoices/edit.html',
            title='Edit Invoice {0}'.format(invoice.name),
            invoice=invoice,
            clients=clients,
            projects=projects
        )


@invoice_blueprint.route(
    '/invoices/delete/<int:invoice_id>', methods=['GET', 'POST'])
@login_required
def delete_invoice(invoice_id):
        invoice = Invoice.query.get(invoice_id)
        if request.method == 'POST':
            db.session.delete(invoice)
            db.session.commit()
            flash("Invoice '{0}' has been deleted.".format(invoice.name))
            return redirect(url_for('invoice.invoices'))
        return render_template(
            'invoices/delete.html',
            title='Delete Invoice {0}'.format(invoice.name),
            invoice=invoice
        )
