# tests/test_invoice.py


import unittest

from base import BaseTestCase
from helpers import add_invoice


class TestInvoiceBlueprint(BaseTestCase):

    def test_invoice_requires_login(self):
        # Ensure /invoices route requres logged in user.
        response = self.client.get('/invoices', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_invoice_with_no_invoices(self):
        # Ensure /invoices shows no clients.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/invoices', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Invoices', response.data)
            self.assertIn(
                "You haven't created any invoices yet.", response.data)

    def test_invoice_with_invoices(self):
        # Ensure /invoices shows one client.
        add_invoice()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/invoices', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Invoices', response.data)
            self.assertIn("<th>False</th>\n", response.data)
            self.assertIn("<th>Real Python</th>\n", response.data)
            self.assertNotIn(
                "You haven't created any invoices yet.", response.data)


if __name__ == '__main__':
    unittest.main()
