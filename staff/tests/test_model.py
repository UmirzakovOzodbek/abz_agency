from ..tests.test_setup import TestSetUp

from ..models import Staff


class StaffModelTest(TestSetUp):

    def test_model_can_create_correctly(self):
        Staff.objects.create(**self.data)
        self.assertEqual(Staff.objects.count(), self.count_staff + 1)

    def test_model_read_correctly(self):
        staff = Staff.objects.get(id=self.staff.id)
        self.assertEqual(staff.id, self.staff.id)
        self.assertEqual(staff.first_name, self.staff.first_name)

    def test_model_update_correctly(self):
        staff = Staff.objects.get(id=self.staff.id)
        staff.first_name = self.data['first_name'] + 'edit'
        staff.save()
        staff = Staff.objects.get(id=self.staff.id)
        self.assertEqual(staff.id, self.staff.id)
        self.assertEqual(staff.first_name, self.data['first_name'] + 'edit')

    def test_model_delete_correctly(self):
        position_at_work = Staff.objects.get(id=self.staff.id)
        position_at_work.delete()
        self.assertEqual(Staff.objects.count(), self.count_staff - 1)
