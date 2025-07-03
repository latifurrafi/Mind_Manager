from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import User, Task


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'password', 'email', 'full_name', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        ("User Information", {"fields": ("username", "email", "full_name")}),
        ("Status", {"fields": ("is_active",)}),
        ("Dates", {"fields": ("created_at",)}),
    )
    readonly_fields = ('created_at',)


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'category', 'due_date', 'time_tracking', 'created_at')
    list_filter = ('priority', 'status', 'category', 'time_tracking', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
    autocomplete_fields = ['user']
    fieldsets = (
        ("Basic Details", {"fields": ("title", "description", "user")}),
        ("Task Settings", {"fields": ("priority", "status", "category", "due_date", "time_tracking")}),
        ("Timestamps", {"fields": ("created_at",)}),
    )
    readonly_fields = ('created_at',)
