# project/invoice/forms.py


from flask_wtf import Form
from wtforms import IntegerField, DateField, StringField
from wtforms.validators import DataRequired, Length


class AddInvoiceForm(Form):
    client = StringField(
        'Client', validators=[DataRequired(), Length(min=3)])
    due_date = DateField(
        'Due Date', validators=[DataRequired(), Length(min=3)])
    total_price = IntegerField(
        'Total Price', validators=[DataRequired(), Length(min=3)])
