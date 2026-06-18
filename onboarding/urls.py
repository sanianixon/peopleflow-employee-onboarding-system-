from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/profile/', views.employee_profile_form, name='employee_profile_form'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('hr/dashboard/', views.hr_dashboard, name='hr_dashboard'),
]