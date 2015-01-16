# tests/helpers.py

import datetime

from project import db
from project.models import Client


def add_client():
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
    db.session.commit()
