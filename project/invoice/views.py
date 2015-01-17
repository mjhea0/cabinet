# project/invoice/views.py


#################
#### imports ####
#################

import datetime

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, abort
from flask.ext.login import login_required

from project import db
from project.models import Invoice, Client
from project.invoice.forms import AddInvoiceForm


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
    invoices = Invoice.query.order_by('due_date').all()
    return render_template(
        'invoices/invoices.html',
        title='Invoices',
        invoices=invoices
    )


@invoice_blueprint.route('/invoices/<int:invoice_id>')
@login_required
def view_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if invoice:
        return render_template(
            'invoices/view.html',
            title=invoice.id,
            invoice=invoice
        )
    else:
        abort(404)


@invoice_blueprint.route('/invoices/create', methods=['GET', 'POST'])
@login_required
def create_invoice():
    form = AddInvoiceForm()
    categories = [(c.id, c.company) for c in Client.query.order_by('company')]
    form.client.choices = categories
    if form.validate_on_submit():
        client = Client.query.get(request.form['client'])
        invoice = Invoice(
            paid=0,
            invoice_date=datetime.datetime.strptime(
                request.form['invoice_date'], '%Y-%m-%d'),
            due_date=datetime.datetime.now(),
            total_price=request.form['total_price'],
            client=client
        )
        db.session.add(invoice)
        db.session.commit()
        flash("Invoice #'{0}' was added for '{1}'.".format(
            invoice.id, client.company),  'success')
        return redirect(url_for('invoice.invoices'))
    return render_template(
        'invoices/create.html',
        title='Add New Invoice',
        form=form
    )


@invoice_blueprint.route(
    '/invoices/edit/<int:invoice_id>', methods=['GET', 'POST'])
@login_required
def edit_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    clients = Client.query.order_by('name')
    if request.method == 'POST':
        client = Client.query.get(request.form['client'])
        invoice.name = request.form['name']
        invoice.currency = request.form['currency']
        invoice.status = request.form['status']
        invoice.notes = request.form['notes']
        invoice.payment = request.form['payment']
        invoice.internal_notes = request.form['internal_notes']
        invoice.client = client
        db.session.add(invoice)
        db.session.commit()
        flash("Invoice '{0}' has been updated.".format(invoice.name))
        return redirect(url_for('invoice.invoices'))
    return render_template(
        'invoices/edit.html',
        title='Edit Invoice {0}'.format(invoice.name),
        invoice=invoice,
        clients=clients,
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
