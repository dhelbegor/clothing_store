from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Avatar'), {'fields': ('avatar',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    filter_horizontal = ('groups',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            self.send_first_access_mail(request, [obj])

    def has_change_permission(self, request, obj=None):
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        if obj and obj.is_superuser and obj.pk != request.user.pk:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        if obj and obj.is_superuser and obj.pk != request.user.pk:
            return False
        if obj and obj.is_staff and obj.pk != request.user.pk and not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return self._get_readonly_fields_for_edit(readonly_fields, request, obj)
        return self._get_readonly_fields_for_add(readonly_fields, request)

    def _get_readonly_fields_for_edit(self, readonly_fields, request, obj):
        if request.user.is_superuser:
            return readonly_fields
        if obj.pk == request.user.pk:
            return readonly_fields + ('groups', 'is_active', 'is_staff', 'is_superuser',)
        if obj.is_staff:
            return readonly_fields + ('email', 'password', 'groups', 'is_active', 'is_staff', 'is_superuser',)
        return readonly_fields + ('is_staff', 'is_superuser',)

    def _get_readonly_fields_for_add(self, readonly_fields, request):
        if request.user.is_superuser:
            return readonly_fields
        return readonly_fields + ('is_staff', 'is_superuser',)
