# project/main/views.py


#################
#### imports ####
#################

from calendar import Calendar
from datetime import date

from flask import render_template, Blueprint
from flask.ext.login import login_required


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('main/home.html', title="Welcome")


@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    cal = Calendar(0)
    year = date.today().year
    month = date.today().month
    cal_list = [cal.monthdatescalendar(year, month)]
    return render_template(
        'main/dashboard.html',
        title='Dashboard',
        year=year,
        this_month=month,
        calendar=cal_list
    )
