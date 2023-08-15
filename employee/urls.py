from django.urls import path
from .views import EmployeeLoginView, EmployeeListCreateView,EmployeeDetailView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login/', EmployeeLoginView.as_view(), name='login-employee'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('list-create/', EmployeeListCreateView.as_view(), name='list-create-employee'),
    path('details/<str:username>', EmployeeDetailView.as_view(), name='details-employee')
]
