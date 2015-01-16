# project/invoice/forms.py


from flask_wtf import Form
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired


class AddInvoiceForm(Form):
    client = SelectField('Client', coerce=int)
    total_price = FloatField('Total Price', validators=[DataRequired()])
