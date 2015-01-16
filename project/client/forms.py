# project/client/forms.py


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length, URL


class AddClientForm(Form):
    first_name = StringField(
        'First Name', validators=[DataRequired(), Length(min=3)])
    last_name = StringField(
        'Last Name', validators=[DataRequired(), Length(min=3)])
    email = StringField(
        'Email Address', validators=[DataRequired(), Email(), Length(min=7)])
    company = StringField(
        'Company Name', validators=[DataRequired(), Length(min=3)])
    website = StringField('Website', validators=[URL()])
    telephone = StringField(
        "Telephone (10-digit)", validators=[Length(min=10, max=10)])
    street = StringField('Street Address')
    city = StringField('City')
    state = StringField('State', validators=[Length(min=2)])
    postal_code = StringField('Postal Code', validators=[Length(min=5)])
    country = StringField('County', validators=[Length(min=2)])
