from django.urls import reverse
from rest_framework.test import APITestCase
from position_at_work.models import PositionAtWork
from ..models import Staff


class TestSetUp(APITestCase):

    def setUp(self) -> None:
        self.data = {'first_name': 'test1',
                     'last_name': 'test1',
                     'patronymic': 'test1',
                     'position_at_work': PositionAtWork.objects.create(title='test_title1'),
                     'wage': 100}

        self.staff = Staff.objects.create(**self.data)
        self.count_staff = Staff.objects.count()
        self.staff_url = reverse('staff')
        self.staff_detail_url = reverse(
            'staff_detail', kwargs={'pk': self.staff.pk})

        return super().setUp()
