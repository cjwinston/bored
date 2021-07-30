import unittest, sys, os

sys.path.append('../bored')
from main import app, db

class UsersTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    ###############
    #### tests ####
    ###############

    def register(self, username, email, password):
        return self.app.post('/register',
                            data=dict(email=email,
                                      password=password, 
                                      confirm_password=password),
                            follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('test@example.com', 'FlaskIsAwesome')
        self.assertEqual(response.status_code, 200)


    def test_invalid_email_registration(self):
        response1 = self.register('test2', 'test@example', 'FlaskIsAwesome')
        self.assertIn(b'Invalid email address.', response1.data)
        response2 = self.register('test2', 'testexample.com', 'FlaskIsAwesome')
        self.assertIn(b'Invalid email address.', response2.data)


    def test_confirm_password_registration(self):
        response1 = self.register('test2', 'test@example', 'FlaskIsAwesome','Flask')
        self.assertIn(b'Field must be equal to password.', response1.data)


if __name__ == "__main__":
    unittest.main()