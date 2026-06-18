from django.contrib import admin
from .models import EmployeeProfile, DocumentType, EmployeeDocument, AuditLog  


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'employee_type', 'joining_date', 'status', 'created_at')
    list_filter = ('status', 'joining_date')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('-created_at',)
    list_filter = ('status', 'employee_type', 'joining_date')


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'required')
    search_fields = ('name',)


@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'document_type', 'status', 'uploaded_at')
    list_filter = ('status', 'document_type')
    search_fields = ('employee__full_name', 'document_type__name')
    ordering = ('-uploaded_at',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'action', 'performed_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('employee__full_name', 'action')
    ordering = ('-created_at',)