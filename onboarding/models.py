from django.db import models
from django.contrib.auth.models import User


class EmployeeProfile(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('SUBMITTED', 'Submitted'),
        ('UNDER_REVIEW', 'Under Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_id = models.CharField(max_length=20, blank=True)
    EMPLOYEE_TYPE_CHOICES = [
        ('FRESHER', 'Fresher'),
        ('EXPERIENCED', 'Experienced'),
    ]

    employee_type = models.CharField(
        max_length=20,
        choices=EMPLOYEE_TYPE_CHOICES,
        default='FRESHER'
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    dob = models.DateField(null=True, blank=True)

    address = models.TextField()

    emergency_contact = models.CharField(max_length=15)

    joining_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EmployeeDocument(models.Model):
    STATUS_CHOICES = [
        ('UPLOADED', 'Uploaded'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='employee_documents/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UPLOADED')
    rejection_reason = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.document_type.name}"
    
class AuditLog(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.action}"