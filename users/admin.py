from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # То что отображается в талблице
    list_display = ('email', 'is_staff', 'is_active',)
    # Фильтр
    list_filter = ('email', 'is_staff', 'is_active',)
    # Item detail
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    # Поисковое поле
    search_fields = ('email',)
    # Сортировка по email
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)