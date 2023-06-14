from django.urls import reverse
from rest_framework.test import APITestCase
from ..models import PositionAtWork


class TestSetUp(APITestCase):

    def setUp(self) -> None:
        self.data = {'title1': 'test_title1', 'title2': 'test_title2'}

        position_at_work = PositionAtWork.objects.create(title=self.data['title1'])
        self.position_id = position_at_work.id
        self.count_position = PositionAtWork.objects.count()
        self.position_url = reverse('position')
        self.position_detail_url = reverse('position_detail', kwargs={'pk': position_at_work.pk})

        return super().setUp()
