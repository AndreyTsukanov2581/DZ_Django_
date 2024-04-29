from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status')
    list_filter = ('status', 'project', 'priority')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Section1', {
            'fields': ('title', 'project',)
        }),
    )
    list_editable = ['status']

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Section1', {
            'fields': ('title', 'project',)
        }),
    )