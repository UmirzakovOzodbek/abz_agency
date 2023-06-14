from rest_framework import serializers

from staff.models import Staff


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ['id', 'image', 'first_name', 'last_name',
                  'patronymic', 'position_at_work',
                  'employment_date', 'wage', 'parent']
