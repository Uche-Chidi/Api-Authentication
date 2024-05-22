from django.urls import path
from . import views


urlpatterns = [
    path('students', views.StudentEndpoint.as_view(), name='students'),
    path('students/<int:pk>', views.StudentDetailEndpoint.as_view(), name='students'),
]