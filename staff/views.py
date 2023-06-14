from staff.models import Staff
from staff.paginations import StandardResultsSetPagination
from staff.serializers import StaffSerializer
from rest_framework.response import Response
from rest_framework import generics, filters


class StaffTreeView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        return Staff.objects.select_related('position_at_work').all()

    def get(self, request):
        qyeryset = self.get_queryset()

        data = []
        for item in qyeryset:
            data.append(self.recursive_subordinate(item))

        return Response(data)

    def recursive_subordinate(self, item):
        result = StaffSerializer(item).data
        subordinate = [self.recursive_subordinate(
            c) for c in item.get_children()]
        if subordinate:
            result["Подчиненный"] = subordinate
        return result


class StaffView(generics.ListCreateAPIView):
    serializer_class = StaffSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'patronymic', 'position_at_work__title', '=employment_date', 'wage',
                     'parent__id']
    ordering_fields = ['first_name', 'last_name', 'patronymic', 'position_at_work__title', 'employment_date', 'wage']
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Staff.objects.select_related('parent', 'position_at_work').all()


class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
