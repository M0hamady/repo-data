from django.contrib import admin

# Register your models here.
from  .models import *
# admin.site.register(User)

from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin


# class CustomUserAdmin(UserAdmin):
#     list_display = (
#         'username', 'email', 'first_name', 'last_name', 'is_staff',
#         'is_accountant', 'is_manager', 'is_designer','is_eng','is_client'
#     )
#     pass

admin.site.register(User,)