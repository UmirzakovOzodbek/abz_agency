from authentication.tests.test_setup import TestSetUp
from rest_framework import status


class TestRegisterViews(TestSetUp):

    def test_user_can_register_without_data(self):
        response = self.client.post(
            self.register_url
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_register_correctly(self):
        response = self.client.post(
            self.register_url,
            self.user_data
        )
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get('token'))


class TestLoginViews(TestSetUp):

    def setUp(self):
        super().setUp()
        self.client.post(
            self.register_url,
            self.user_data
        )

    def test_user_can_login_without_data(self):
        response = self.client.post(
            self.login_url
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_login_correctly(self):
        data = {
            'username': self.user_data.get('username'),
            'password': self.user_data.get('password')
        }
        response = self.client.post(
            self.login_url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get('token'))

    def test_user_can_login_incorrect_data(self):
        data = {
            'username': self.user_data.get('username') + '1',
            'password': self.user_data.get('password')
        }
        response = self.client.post(
            self.login_url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
