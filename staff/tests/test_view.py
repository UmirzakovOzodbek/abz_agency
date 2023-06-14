from position_at_work.models import PositionAtWork
from staff.tests.test_setup import TestSetUp
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


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

    def test_staff_can_create_without_data(self):
        response = self.client.post(
            self.staff_url
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_staff_can_create_correctly(self):
        data = {'first_name': 'test2',
                'last_name': 'test2',
                'patronymic': 'test2',
                'position_at_work': PositionAtWork.objects.get(title='test_title1').id,
                'wage': 100}
        response = self.client.post(
            self.staff_url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_staff_can_read_correctly(self):
        response = self.client.get(
            self.staff_url
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), self.count_staff)

    def test_staff_detail_update_correctly(self):
        data = {'first_name': 'test3',
                'last_name': 'test3',
                'patronymic': 'test3',
                'position_at_work': PositionAtWork.objects.get(title='test_title1').id,
                'wage': 100}
        response = self.client.put(
            self.staff_detail_url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_position_at_work_detail_patch_correctly(self):
        data = {'first_name': 'test3'}
        response = self.client.patch(
            self.staff_detail_url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], data['first_name'])

    def test_position_at_work_detail_delete_correctly(self):
        response = self.client.delete(
            self.staff_detail_url
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
