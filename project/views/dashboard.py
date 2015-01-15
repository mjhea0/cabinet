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
		return redirect(url_for('user.login'))

