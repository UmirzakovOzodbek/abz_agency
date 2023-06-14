import pdb
from ..tests.test_setup import TestSetUp
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class TestPositionAtWorkViews(TestSetUp):

    def setUp(self) -> None:
        super().setUp()

        user_data = {
            'email': 'pgadmin4@pgadmin.org',
            'username': 'email1',
            'password': 'qw1easdzx'
        }

        user = User.objects.create_superuser(**user_data)
        token = Token.objects.create(user=user)

        self.client = APIClient(
            HTTP_AUTHORIZATION='Bearer {}'.format(token.key))

    def test_position_at_work_can_create_without_data(self):
        response = self.client.post(
            self.position_url
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_position_at_work_can_create_correctly(self):
        data = {'title': self.data['title2']}
        response = self.client.post(
            self.position_url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_position_at_work_can_read_correctly(self):
        response = self.client.get(
            self.position_url
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.count_position)

    def test_position_at_work_detail_read_correctly(self):
        response = self.client.get(
            self.position_detail_url
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test_title1')

    def test_position_at_work_detail_update_correctly(self):
        response = self.client.put(
            self.position_detail_url,
            {'title': self.data['title2']}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test_title2')

    def test_position_at_work_detail_patch_correctly(self):
        response = self.client.patch(
            self.position_detail_url,
            {'title': self.data['title2']}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test_title2')

    def test_position_at_work_detail_delete_correctly(self):
        response = self.client.delete(
            self.position_detail_url
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
