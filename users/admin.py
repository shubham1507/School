from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Teacher


class TeacherProfileInline(admin.StackedInline):
    model = Teacher
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Personal info'), {
            'fields': ('address', 'phone_number')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions')
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'password1', 'password2'),
    }), )
    list_display = ('email', 'first_name', 'last_name', 'address',
                    'phone_number', 'is_staff')
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'address',
        'phone_number',
    )
    ordering = ('email', )
    inlines = (TeacherProfileInline, )