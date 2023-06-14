from django.urls import path
from staff import views


urlpatterns = [
    path('tree/', views.StaffTreeView.as_view(), name='staff_tree'),
    path('', views.StaffView.as_view(), name='staff'),
    path('<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),
]
