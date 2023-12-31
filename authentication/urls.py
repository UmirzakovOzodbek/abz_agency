from django.urls import path

from authentication.views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]