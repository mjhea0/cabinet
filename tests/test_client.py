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

    def test_create_client_login(self):
        # Ensure /clients/create route requres logged in user.
        add_client()
        response = self.client.get('/clients/create', follow_redirects=True)
        self.assertIn('Please log in to access tis page', response.data)



# @client_blueprint.route('/clients/create', methods=['GET', 'POST'])
# @login_required
# def create_client():
#     form = AddClientForm()
#     if form.validate_on_submit():
#         client = Client(
#             first_name=request.form['first_name'],
#             last_name=request.form['last_name'],
#             email=request.form['email'],
#             company=request.form['company'],
#             website=request.form['website'],
#             telephone=request.form['telephone'],
#             street=request.form['street'],
#             city=request.form['city'],
#             state=request.form['state'],
#             postal_code=request.form['postal_code'],
#             country=request.form['country'],
#             date_created=datetime.datetime.now()
#         )
#         db.session.add(client)
#         db.session.commit()
#         flash("Client '{0}' was added.".format(client.company), 'success')
#         return redirect(url_for('client.clients'))
#     return render_template('clients/create.html', title="Add Client", form=form)

if __name__ == '__main__':
    unittest.main()
