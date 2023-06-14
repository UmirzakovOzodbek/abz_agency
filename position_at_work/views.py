from rest_framework import generics

from position_at_work.models import PositionAtWork
from position_at_work.serializers import PositionAtWorkSerializer


class PositionAtWorkView(generics.ListCreateAPIView):

    queryset = PositionAtWork.objects.all()
    serializer_class = PositionAtWorkSerializer


class PositionAtWorkDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PositionAtWork.objects.all()
    serializer_class = PositionAtWorkSerializer
