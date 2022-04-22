from django.urls import path
from . import views


app_name = "school_details"   


urlpatterns = [
    
    path('student/', views.student_details, name="student"),
    path('register/', views.register_request, name="register"),
    path('home/',views.home,name='home'),
    path('login/', views.login_user, name="login"),
    path('student/logout/',views.logout_user,name='logout'),
    path('student_data/',views.student_data,name='student_data'),
    path('indi_data/',views.indi_data,name='indi_data'),
    path('complete_data/<int:id>/', views.complete_data, name='complete_data'),
    path('Student_field/',views.Student_field, name='Student_field'),
    path('teacher_field/',views.teacher_field, name='teacher_field'),
    path('success',views.success,name='success'),
    path('edit/<int:id>/',views.edit,name='edit'),

]


    