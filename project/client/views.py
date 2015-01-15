# project/client/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask.ext.login import login_required

from project import db
from project.models import Client


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
    clients = Client.query.order_by('name').all()
    return render_template(
        'clients/clients.html',
        title='Clients',
        clients=clients
    )


@client_blueprint.route('/clients/<int:client_id>')
@login_required
def view_client(client_id):
    client = Client.query.get(client_id)
    projects = client.projects.all()
    invoices = client.invoices.all()
    return render_template(
        'clients/view.html',
        title=client.name,
        client=client,
        projects=projects,
        invoices=invoices
    )


@client_blueprint.route('/clients/create', methods=['GET', 'POST'])
@login_required
def create_client():
    if request.method == 'POST':
        client = Client(
            name=request.form['name'],
            company=request.form['company'],
            website=request.form['website'],
            twitter=request.form['twitter'],
            email=request.form['email'],
            telephone=request.form['telephone'],
            skype=request.form['skype'],
            street=request.form['street'],
            street_2=request.form['street_2'],
            city=request.form['city'],
            state=request.form['state'],
            postcode=request.form['postcode'],
            country=request.form['country'],
            notes=request.form['notes'])
        db.session.add(client)
        db.session.commit()
        flash("Client '{0}' was added.".format(client.name))
        return redirect(url_for('client.clients'))
    return render_template('clients/create.html')


@client_blueprint.route(
    '/clients/edit/<int:client_id>', methods=['GET', 'POST'])
@login_required
def edit_client(client_id):
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
        return redirect(url_for('client.clients'))
    return render_template(
        'clients/edit.html',
        title='Edit {0}'.format(client.name),
        client=client
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
