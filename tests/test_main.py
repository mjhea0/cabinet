# tests/test_main.py


import unittest

from base import BaseTestCase


class TestMainBlueprint(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get(
            '/', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please log in to access this page.', response.data)


if __name__ == '__main__':
    unittest.main()
