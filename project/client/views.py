# project/client/views.py


#################
#### imports ####
#################

import datetime

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask.ext.login import login_required

from project import db
from project.models import Client
from project.client.forms import AddClientForm


################
#### config ####
################

client_blueprint = Blueprint('client', __name__,)


################
#### routes ####
################

@client_blueprint.route('/clients')
@login_required
def clients():
    clients = Client.query.order_by('last_name').all()
    return render_template(
        'clients/clients.html',
        title='Clients',
        clients=clients
    )


@client_blueprint.route('/clients/<int:client_id>')
@login_required
def view_client(client_id):
    client = Client.query.get(client_id)
    invoices = client.invoices.all()
    return render_template(
        'clients/view.html',
        title=client.company,
        client=client,
        invoices=invoices
    )


@client_blueprint.route('/clients/create', methods=['GET', 'POST'])
@login_required
def create_client():
    form = AddClientForm()
    if form.validate_on_submit():
        client = Client(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            company=request.form['company'],
            website=request.form['website'],
            telephone=request.form['telephone'],
            street=request.form['street'],
            city=request.form['city'],
            state=request.form['state'],
            postal_code=request.form['postal_code'],
            country=request.form['country'],
            date_created=datetime.datetime.now()
        )
        db.session.add(client)
        db.session.commit()
        flash("Client '{0} {1}' was added.".format(
            client.first_name, client.last_name), 'success')
        return redirect(url_for('client.clients'))
    return render_template('clients/create.html', title="Add Client", form=form)


@client_blueprint.route(
    '/clients/edit/<int:client_id>', methods=['GET', 'POST'])
@login_required
def edit_client(client_id):
    form = AddClientForm()
    client = Client.query.get(client_id)
    if form.validate_on_submit():
        client.first_name = request.form['first_name']
        client.last_name = request.form['last_name']
        client.email = request.form['email']
        client.company = request.form['company']
        client.website = request.form['website']
        client.telephone = request.form['telephone']
        client.street = request.form['street']
        client.city = request.form['city']
        client.state = request.form['state']
        client.postal_code = request.form['postal_code']
        client.country = request.form['country']
        db.session.add(client)
        db.session.commit()
        flash("Client '{0} {1}' has been updated.".format(
            client.first_name, client.last_name), 'success')
        return redirect(url_for('client.clients'))
    return render_template(
        'clients/edit.html',
        title='Edit {0}'.format(client.company),
        client=client,
        form=form
    )


@client_blueprint.route(
    '/clients/delete/<int:client_id>', methods=['GET', 'POST'])
def delete_client(client_id):
        client = Client.query.get(client_id)
        if request.method == 'POST':
            db.session.delete(client)
            db.session.commit()
            flash("Client '{0}' has been deleted.".format(client.name))
            return redirect(url_for('client.clients'))
        return render_template(
            'clients/delete.html',
            title='Delete {0}'.format(client.name),
            client=client
        )
