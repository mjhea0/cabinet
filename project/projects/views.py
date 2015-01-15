# project/projects/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask.ext.login import login_required

from project import db
from project.models import Project, Client


################
#### config ####
################

projects_blueprint = Blueprint('projects', __name__,)


################
#### routes ####
################

@projects_blueprint.route('/projects')
@login_required
def projects():
    projects = Project.query.order_by('name')
    return render_template(
        'projects/projects.html',
        title='projects',
        projects=projects
    )


@projects_blueprint.route('/projects/<int:project_id>')
@login_required
def view_project(project_id):
    project = Project.query.get(project_id)
    return render_template(
        'projects/view.html',
        title=project.name,
        project=project
    )


@projects_blueprint.route('/projects/create', methods=['GET', 'POST'])
@login_required
def create_project():
    clients = Client.query.order_by('name')
    if request.method == 'POST':
        client = Client.query.get(request.form['client'])
        project = Project(
            name=request.form['name'],
            description=request.form['description'],
            status=request.form['status'],
            hourly_rate=request.form['hourly_rate'],
            quote=request.form['quote'],
            notes=request.form['notes'],
            client=client)
        db.session.add(project)
        db.session.commit()
        flash("Project '{0}' was added.".format(project.name))
        return redirect(url_for('projects.projects'))
    return render_template(
        'projects/create.html',
        title='Add a New Project',
        clients=clients
    )


@projects_blueprint.route(
    '/projects/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get(project_id)
    clients = Client.query.order_by('name')
    if request.method == 'POST':
        client = Client.query.get(request.form['client'])
        project.name = request.form['name']
        project.description = request.form['description']
        project.status = request.form['status']
        project.hourly_rate = request.form['hourly_rate']
        project.quote = request.form['quote']
        project.notes = request.form['notes']
        project.client = client
        db.session.add(project)
        db.session.commit()
        flash("Project '{0}' has been updated.".format(project.name))
        return redirect(url_for('projects.projects'))
    return render_template(
        'projects/edit.html',
        title='Edit {0}'.format(project.name),
        project=project,
        clients=clients
    )


@projects_blueprint.route(
    '/projects/delete/<int:project_id>', methods=['GET', 'POST'])
@login_required
def delete_project(project_id):
        project = Project.query.get(project_id)
        if request.method == 'POST':
            db.session.delete(project)
            db.session.commit()
            flash("Project '{0}' has been deleted.".format(project.name))
            return redirect(url_for('projects.projects'))
        return render_template(
            'projects/delete.html',
            title='Delete {0}'.format(project.name),
            project=project
        )
