from django.contrib import admin
from accounts.models.models import User
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)
from django.utils.translation import gettext_lazy as _

# Register your models here.
class UserAdmin(BaseUserAdmin):
    """Define the admin page for users."""
    ordering = ["email"]
    list_display = ["first_name", "last_name", "email", "phone_number"]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'), 
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'phone_number',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important dates'), {'fields': ('last_login',)}
        ),
    )
    readonly_fields = ['last_login', 'id']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

admin.site.register(User, UserAdmin)