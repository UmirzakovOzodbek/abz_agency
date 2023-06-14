from random import choice, randint
from django.core.management.base import BaseCommand

from staff.models import Staff
from position_at_work.models import PositionAtWork


class Command(BaseCommand):
    help = "create 50_000 staff"

    def __init__(self):
        super().__init__()
        self.position_at_work = [{'id': 1, 'title': 'Директор подразделения'},
                                 {'id': 2, 'title': 'Начальник подразделения'},
                                 {'id': 3, 'title': 'Начальник группы'},
                                 {'id': 4, 'title': 'Начальник отдела'},
                                 {'id': 5, 'title': 'Работник'},
                                 ]
        self.position_at_work_list = []
        self.first_name = ['Илья', 'Вадим', 'Алексей']
        self.last_name = ['Кондратьев', 'Николаев', 'Константинов']
        self.patronymic = ['Владимирович', 'Семенович', 'Альбертович']
        self.staff_parent = []

    def handle(self, *args, **options):
        self.stdout.write('seeding start')

        self.clear_model()

        self.create_position_at_work()

        self.create_staff()

        self.stdout.write('done.')

    def clear_model(self):
        Staff.objects.all().delete()
        PositionAtWork.objects.all().delete()

    def create_position_at_work(self):
        for item in self.position_at_work:
            self.position_at_work_list.append(
                PositionAtWork(
                    item['id'],
                    item['title']
                )
            )
        PositionAtWork.objects.bulk_create(self.position_at_work_list)

    def create_staff(self):

        self.create_personal_staff(100)

        self.create_personal_staff(900)

        self.create_personal_staff(4_000)

        self.create_personal_staff(15_000)

        self.create_personal_staff(30_000)

    def create_personal_staff(self, number):
        current_staff = []

        for _ in range(number):
            staff = Staff(first_name=choice(self.first_name),
                          last_name=choice(self.last_name),
                          patronymic=choice(self.patronymic),
                          position_at_work=choice(self.position_at_work_list),
                          wage=randint(10_000, 1_000_000),
                          parent=choice(
                          self.staff_parent) if self.staff_parent else None,
                          )
            staff.save()
            current_staff.append(staff)
        # Staff.objects.bulk_create(current_staff)
        self.staff_parent = current_staff
        self.stdout.write(f'Succees {number}')
