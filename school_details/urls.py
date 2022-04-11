from django.urls import path
from . import views
# from school_details.views import StudentData

app_name = "school_details"   


urlpatterns = [
    
    
    path('register/', views.register_request, name="register"),
    path('home/',views.home,name='home'),
    
    path('student/', views.student_details, name="student"),
    path('login/', views.login_user, name="login"),
    path('student/logout/',views.logout_user,name='logout'),
    path('student_data/',views.student_data,name='student_data'),
    path('indi_data/',views.indi_data,name='indi_data'),
    path('complete_data/<int:pk>/', views.complete_data, name='complete_data'),
]


    