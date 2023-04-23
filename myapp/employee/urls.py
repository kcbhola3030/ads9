# urls.py

from django.urls import path
from .views import EmployeeList, EmployeeDetail,EmployeeCreateView

urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view()),
    path('employees/add',EmployeeCreateView.as_view())
]
