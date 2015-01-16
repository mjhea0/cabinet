# tests/test_client.py


import unittest

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
            response = self.client.post(
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
            response = self.client.post(
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
            response = self.client.post(
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
            response = self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/1', follow_redirects=True)
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
