
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserForm,StudentForm,StudentDetailsForm
from .models import CustomUser,Subject,Mark

admin.site.register(CustomUser)   
admin.site.register(Subject)
admin.site.register(Mark)