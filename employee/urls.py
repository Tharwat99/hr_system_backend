from django.urls import path
from .views import EmployeeLoginView, EmployeeListCreateView,EmployeeDetailView


urlpatterns = [
    path('login/', EmployeeLoginView.as_view(), name='login-employee'),
    path('logout/', EmployeeLoginView.as_view(), name='logout-employee'),
    path('list-create/', EmployeeListCreateView.as_view(), name='list-create-employee'),
    path('details/<str:username>', EmployeeDetailView.as_view(), name='details-employee')
]
