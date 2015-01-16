# tests/test_client.py


import unittest

from base import BaseTestCase


class TestClientBlueprint(BaseTestCase):

    def test_clients_login(self):
        # Ensure /clients shows now clients.
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

    def test_client_requires_login(self):
        # Ensure /clients route requres logged in user.
        response = self.client.get('/clients', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)


if __name__ == '__main__':
    unittest.main()
