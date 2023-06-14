from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class BbAdmin (admin. ModelAdmin) :
    list_display = ('first_name', 'last_name', 'patronymic',)

    list_filter = (
        'position_at_work__title',
    )
