from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = ("username", "first_name", "last_name" , "is_staff", "is_active",)
    list_filter = ("username", "first_name", "last_name" , "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "first_name", "last_name", "address","password" )}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )




# Register your models here.
admin.site.register(CustomUserModel, CustomUserAdmin)
