from django.test import TestCase
from api.models import User
from rest_framework.test import APIClient

class TestView(TestCase):

    def setup(self):
        pass

    def testView(self):
        client = APIClient()
        response = client.post('/auth/login/', {'username': 'john', 'password': 'smith'})
        assert response.status_code == 200



    