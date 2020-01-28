from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'username', 'name', 'surname', 'phone')
    list_filter = ('email', 'is_staff', 'is_active', 'username', 'name', 'surname', 'phone')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'name', 'surname', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'name', 'surname',)
    ordering = ('email','username', 'name', 'surname',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
