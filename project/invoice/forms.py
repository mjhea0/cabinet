# project/invoice/forms.py


from flask_wtf import Form
from wtforms import FloatField, DateField, SelectField
from wtforms.validators import DataRequired, Length


class AddInvoiceForm(Form):
    client = SelectField('Client')
    due_date = DateField('Due Date', validators=[DataRequired(), Length(min=3)])
    total_price = FloatField('Total Price', validators=[DataRequired()])
