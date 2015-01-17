# tests/test_client.py


import unittest
import datetime

from base import BaseTestCase
from helpers import add_data


class TestClientBlueprint(BaseTestCase):

    def test_client_requires_login(self):
        # Ensure /clients route requres logged in user.
        response = self.client.get('/clients', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_client_with_no_clients(self):
        # Ensure /clients shows no clients.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("You haven't created any clients yet.", response.data)

    def test_client_with_clients(self):
        # Ensure /clients shows one client.
        add_data()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("<th>Michael</th>", response.data)
            self.assertIn("<th>1</th>", response.data)
            self.assertNotIn("<th>2</th>", response.data)

    def test_client_view_login(self):
        # Ensure /clients/<int:client_id> route requres logged in user.
        add_data()
        response = self.client.get('/clients/1', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_client_view(self):
        # Ensure /clients/1 route exists.
        add_data()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/1', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("Real Python", response.data)

    def test_client_view_with_no_clients(self):
        # Ensure /clients/1 route does not exist.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/1', follow_redirects=True)
            self.assertEqual(response.status_code, 404)

    def test_client_view_with_invoices(self):
        pass

    def test_client_create_login(self):
        # Ensure /clients/create route requres logged in user.
        response = self.client.get('/clients/create', follow_redirects=True)
        self.assertIn('Please log in to access this page', response.data)

    def test_client_create_route(self):
        # Ensure /clients/create exists.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/clients/create', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("Add Client", response.data)

    def test_client_create(self):
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
            self.assertEqual(response.status_code, 200)
            self.assertIn("Client &#39;company&#39; was added.", response.data)

    def test_client_create_errors(self):
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
            self.assertEqual(response.status_code, 200)
            self.assertIn('This field is required.', response.data)

    def test_client_edit_login(self):
        # Ensure clients/edit/1 route requres logged in user.
        add_data()
        response = self.client.get('/clients/edit/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please log in to access this page', response.data)

    def test_client_edit(self):
        #  Ensure client can be edited (clients/edit/1).
        add_data()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.post(
                '/clients/edit/1',
                data=dict(
                    first_name='new_first_name',
                    last_name='new_last_name',
                    email='new_email@new_email.com',
                    company='new_company',
                    website='http://new_website.com',
                    telephone='5556667777',
                    street='new_street',
                    city='new_city',
                    state='new_state',
                    postal_code='78978',
                    country='new_country',
                    date_created=datetime.datetime.now()
                ),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                'Client &#39;new_company&#39; was updated.', response.data)

    def test_client_edit_errors(self):
        #  Ensure errors populate (clients/edit/1).
        add_data()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.post(
                '/clients/edit/1',
                data=dict(
                    first_name='new_first_name',
                    last_name='',
                    email='new_email@new_email.com',
                    company='new_company',
                    website='http://new_website.com',
                    telephone='5556667777',
                    street='new_street',
                    city='new_city',
                    state='new_state',
                    postal_code='78978',
                    country='new_country',
                    date_created=datetime.datetime.now()
                ),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn("This field is required.", response.data)

    def test_client_delete_login(self):
        # Ensure clients/delete/1 route requres logged in user.
        add_data()
        response = self.client.get('/clients/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please log in to access this page', response.data)

    def test_client_delete_route(self):
        #  Ensure cclients/delete/1 route is accesible.
        add_data()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get(
                '/clients/delete/1', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                'Are you sure you want to delete client <em>Real Python</em>?',
                response.data)

    def test_client_delete(self):
        #  Ensure client can be deleted (clients/delete/1).
        add_data()
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.post(
                '/clients/delete/1', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                'Client &#39;Real Python&#39; was deleted.\n', response.data)

# @client_blueprint.route(
#     '/clients/delete/<int:client_id>', methods=['GET', 'POST'])
# def delete_client(client_id):
#     client = Client.query.get(client_id)
#     if request.method == 'POST':
#         db.session.delete(client)
#         db.session.commit()
#         flash("Client '{0}' was deleted.".format(client.company), 'success')
#         return redirect(url_for('client.clients'))
#     return render_template(
#         'clients/delete.html',
#         title='Delete {0}'.format(client.company),
#         client=client
#     )


if __name__ == '__main__':
    unittest.main()
