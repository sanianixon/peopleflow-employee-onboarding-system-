from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import EmployeeProfile, EmployeeDocument


def home(request):
    return render(request, 'onboarding/home.html')


def employee_profile_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        user = User.objects.create_user(
            username=email,
            email=email,
            password='test123'
        )

        EmployeeProfile.objects.create(
            user=user,
            full_name=request.POST.get('full_name'),
            email=email,
            phone=request.POST.get('phone'),
            employee_type=request.POST.get('employee_type'),
            address=request.POST.get('address'),
            emergency_contact=request.POST.get('emergency_contact'),
            joining_date=request.POST.get('joining_date') or None,
            status='SUBMITTED'
        )

        return redirect('employee_dashboard')

    return render(request, 'onboarding/employee_form.html')


def employee_dashboard(request):
    employee = EmployeeProfile.objects.last()
    documents = EmployeeDocument.objects.filter(employee=employee) if employee else []

    return render(request, 'onboarding/employee_dashboard.html', {
        'employee': employee,
        'documents': documents
    })


def hr_dashboard(request):
    employees = EmployeeProfile.objects.all().order_by('-created_at')

    return render(request, 'onboarding/hr_dashboard.html', {
        'employees': employees
    })