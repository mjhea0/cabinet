from flask import render_template, session, redirect, url_for, request, flash
from app import app, db
from app.models import Project, Client

@app.route('/projects')
def projects():
	if session.get('username'):
		projects = Project.query.order_by('name')
		return render_template('projects/projects.html',
			title = 'projects',
			projects = projects)
	else:
		return redirect(url_for('login'))

@app.route('/projects/<int:project_id>')
def view_project(project_id):
	if session.get('username'):
		project = Project.query.get(project_id)
		return render_template('projects/view.html',
			title = project.name,
			project = project)
	else:
		return redirect(url_for('login'))

@app.route('/projects/create', methods = ['GET', 'POST'])
def create_project():
	if session.get('username'):
		clients = Client.query.order_by('name')
		if request.method == 'POST':
			client = Client.query.get(request.form['client'])
			project = Project(
				name = request.form['name'],
				client = client)
			db.session.add(project)
			db.session.commit()
			flash("Project '%s' was added." % project.name)
			return redirect(url_for('projects'))
		return render_template('projects/create.html',
			title = 'Add a New Project',
			clients = clients)
	else:
		return redirect(url_for('login'))

@app.route('/projects/edit/<int:project_id>', methods = ['GET', 'POST'])
def edit_project(project_id):
	if session.get('username'):
		project = Project.query.get(project_id)
		clients = Client.query.order_by('name')
		if request.method == 'POST':
			client = Client.query.get(request.form['client'])
			project.name = request.form['name']
			project.client = client
			db.session.add(project)
			db.session.commit()
			flash("Project '%s' has been updated." % project.name)
			return redirect(url_for('projects'))
		return render_template('projects/edit.html',
			title = 'Edit %s' % project.name,
			project = project,
			clients = clients)
	else:
		return redirect(url_for('login'))

@app.route('/projects/delete/<int:project_id>', methods = ['GET', 'POST'])
def delete_project(project_id):
	if session.get('username'):
		project = Project.query.get(project_id)
		if request.method == 'POST':
			db.session.delete(project)
			db.session.commit()
			flash("Project '%s' has been deleted." % project.name)
			return redirect(url_for('projects'))
		return render_template('projects/delete.html',
			title = 'Delete %s' % project.name,
			project = project)
	else:
		return redirect(url_for('login'))