import unittest
from src.app import create_app, db
from src.app.models import Event, Availability

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_event_creation(self):
        response = self.client.post('/', data={'name': 'My Event'})
        self.assertEqual(response.status_code, 302)  # Redirect after creation
