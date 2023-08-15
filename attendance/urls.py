from django.urls import path
from .views import AttendanceListCreateView


urlpatterns = [
    path('list-create/', AttendanceListCreateView.as_view(), name='list-create-attendance')
]
