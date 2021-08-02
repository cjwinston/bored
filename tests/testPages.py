import unittest, sys

sys.path.append('../bored') # imports python file from parent directory
from main import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_signup_page(self):
        response = self.app.get('/signup', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_trivia_page(self):
        response = self.app.get('/trivia', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_events_page(self):
        response = self.app.get('/events', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_movietv_page(self):
        response = self.app.get('/movietv', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()