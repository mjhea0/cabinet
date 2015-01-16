# tests/test_client.py


import unittest
import datetime

from base import BaseTestCase
from helpers import add_client


class TestClientBlueprint(BaseTestCase):

    def test_client_requires_login(self):
        # Ensure /clients route requres logged in user.
        response = self.client.get('/clients', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_clients_with_no_clients(self):
        # Ensure /clients shows no clients.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Clients', response.data)
            self.assertIn("You haven't created any clients yet.", response.data)

    def test_clients_with_clients(self):
        # Ensure /clients shows one client.
        add_client()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Clients', response.data)
            self.assertIn("<th>Michael</th>", response.data)
            self.assertIn("<th>1</th>", response.data)
            self.assertNotIn("<th>2</th>", response.data)

    def test_view_client_login(self):
        # Ensure /clients/<int:client_id> route requres logged in user.
        add_client()
        response = self.client.get('/clients/1', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_view_client(self):
        # Ensure /clients/1 route exists.
        add_client()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/1', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Clients', response.data)
            self.assertIn("Real Python", response.data)

    def test_view_client_with_no_clients(self):
        # Ensure /clients/1 route does not exist.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/1', follow_redirects=True)
            self.assertEqual(response.status_code, 404)

    def test_view_client_with_invoices(self):
        pass

    def test_create_client_login(self):
        # Ensure /clients/create route requres logged in user.
        add_client()
        response = self.client.get('/clients/create', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_create_client(self):
        # Ensure /clients/create exists.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/create', follow_redirects=True)
            self.assertIn('Clients', response.data)
            self.assertIn("Add Client", response.data)

    def test_create_client_post(self):
        #  Ensure new client can be created.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.post(
                '/clients/create',
                data=dict(
                    first_name='first_name',
                    last_name='last_name',
                    email='email@email.com',
                    company='company',
                    website='http://website.com',
                    telephone='1112221234',
                    street='street',
                    city='city',
                    state='state',
                    postal_code='60987',
                    country='country',
                    date_created=datetime.datetime.now()
                ),
                follow_redirects=True
            )
            self.assertIn('Clients', response.data)
            self.assertIn("Client &#39;company&#39; was added.", response.data)

    def test_create_client_post_errors(self):
        #  Ensure errors populate.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.post(
                '/clients/create',
                data=dict(
                    first_name='',
                    last_name='last_name',
                    email='email@email.com',
                    company='company',
                    website='http://website.com',
                    telephone='1112221234',
                    street='street',
                    city='city',
                    state='state',
                    postal_code='60987',
                    country='country',
                    date_created=datetime.datetime.now()
                ),
                follow_redirects=True
            )
            self.assertIn('Clients', response.data)
            self.assertIn("This field is required.", response.data)


if __name__ == '__main__':
    unittest.main()
