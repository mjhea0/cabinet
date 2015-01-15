from flask import render_template, session, redirect, url_for, request
from calendar import Calendar
from datetime import date
from project import app

@app.route('/')
@app.route('/index')
def index():
	# check if user is logged in
	if session.get('username'):
		cal = Calendar(0)
		year = date.today().year
		month = date.today().month
#		cal_list = [cal.monthdatescalendar(year, i + 1) for i in xrange(12)]
		cal_list = [cal.monthdatescalendar(year, month)]
		return render_template('index.html',
			title = 'Dashboard',
			year = year,
			this_month = month,
			calendar = cal_list)
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