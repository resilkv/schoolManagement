
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserForm,StudentForm,StudentDetailsForm,TeacherForm,StudentForm
from .models import CustomUser,Subject,Mark,Grade,Student,Teacher

admin.site.register(CustomUser)   
admin.site.register(Subject)
admin.site.register(Mark)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Teacher)