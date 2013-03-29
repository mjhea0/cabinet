from flask import render_template, session, redirect, url_for, request
from app import app

@app.route('/')
@app.route('/index')
def index():
	# check if user is logged in
	if session.get('username'):
		return render_template('index.html',
			title = 'Dashboard',
			username = session['username'])
	else:
		return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = 0
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['username'] = request.form['username']
			return redirect(url_for('index'))
	return render_template('login.html',
		title = 'Login', error = error)

@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('login'))