from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date') # Display these fields in the admin list view
    list_filter = ('author', 'publication_year')  # Add filters for these fields
    search_fields = ('title', 'author') # Enable search capabilities for these fields

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
