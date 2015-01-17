# project/invoice/forms.py


import datetime

from flask_wtf import Form
from wtforms import FloatField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class AddInvoiceForm(Form):
    client = SelectField('Client', coerce=int)
    total_price = FloatField('Total Price', validators=[DataRequired()])
    invoice_date = DateField(
        'Invoice Date', format='%Y-%m-%d', default=datetime.datetime.now())
