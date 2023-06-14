from rest_framework import serializers
from position_at_work.models import PositionAtWork


class PositionAtWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionAtWork
        fields = '__all__'
