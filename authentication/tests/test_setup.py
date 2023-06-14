from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):

    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'email': 'pgadmin4@pgadmin.org',
            'username': 'email1',
            'password': 'qw1easdzx'
        }
        return super().setUp()
