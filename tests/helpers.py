# tests/helpers.py

import datetime

from project import db
from project.models import Client, Invoice


def add_data():
    client = Client(
        first_name='Michael',
        last_name='Herman',
        email='michael@realpython.com',
        company='Real Python',
        website='https://realpython.com',
        telephone='415XXXXXX',
        street='210 3rd Ave #1',
        city='San Francisco',
        state='CA',
        postal_code='94122',
        country='United States',
        date_created=datetime.datetime.now()
    )
    db.session.add(client)
    client = Client.query.first()
    invoice = Invoice(
        paid=0,
        invoice_date=datetime.datetime.now(),
        due_date=datetime.datetime.now(),
        total_price=22.00,
        client=client
    )
    db.session.add(invoice)
    db.session.commit()
