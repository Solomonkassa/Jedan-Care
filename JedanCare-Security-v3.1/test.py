import unittest
from flask import current_app
from app import create_app, db

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_contact_route(self):
        response = self.app.test_client().get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Form', response.data)

    # Add more test cases for other routes and functionality

if __name__ == '__main__':
    unittest.main()

