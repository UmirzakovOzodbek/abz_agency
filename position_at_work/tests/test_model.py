from ..tests.test_setup import TestSetUp

from ..models import PositionAtWork

class PositionAtWorkModelTest(TestSetUp):

    def test_model_can_create_correctly(self):
        PositionAtWork.objects.create(title=self.data['title2'])
        self.assertEqual(PositionAtWork.objects.count(), self.count_position + 1)

    def test_model_read_correctly(self):
        position_at_work = PositionAtWork.objects.get(id=self.position_id)
        self.assertEqual(position_at_work.id, self.position_id)
        self.assertEqual(position_at_work.title, self.data['title1'])

    def test_model_update_correctly(self):
        position_at_work = PositionAtWork.objects.get(id=self.position_id)
        position_at_work.title = self.data['title2']
        position_at_work.save()
        position_at_work = PositionAtWork.objects.get(id=self.position_id)
        self.assertEqual(position_at_work.id, self.position_id)
        self.assertEqual(position_at_work.title, self.data['title2'])

    def test_model_delete_correctly(self):
        position_at_work = PositionAtWork.objects.get(id=self.position_id)
        position_at_work.delete()
        self.assertEqual(PositionAtWork.objects.count(), self.count_position - 1)
