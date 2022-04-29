from django.shortcuts import  render, redirect,HttpResponse
from .forms import NewUserForm,StudentForm,StudentDetailsForm,StudentFieldForm,TeacherForm,SingleStudentForm,MarkForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import CustomUser,Mark,Grade,Student,Teacher
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from smtplib import SMTP
import smtplib
# from celery.decorators import task
from school2.settings import EMAIL_HOST_USER
from celery.utils.log import get_task_logger
from . task import send_mail_to



def register_request(request):
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful." )
            if user.category=='student':
                return redirect("/Student_field")
            else:
                return redirect('/teacher_field')   
            login(request, user)    
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def home(request):
    if request.user.is_authenticated:
        return render(request,'user_home.html')
    return render(request,'home.html')


def check_role_user(login_user):
    if login_user.is_authenticated and (login_user.category=='teacher' or login_user.is_superuser):
        return True
    else:
        return False 

 
@login_required(login_url=None)
@user_passes_test(check_role_user,login_url='/')
def student_details(request):
    # import pdb;pdb.set_trace() 
    user=request.user
    teacher=user.teacher
    teacher_grade=Grade.objects.filter(teacher=teacher)
    grade_id=list(teacher_grade.values_list('id',flat=True))
    student=Student.objects.filter(grade__in=grade_id)
    student_id=list(student.values_list('user_id',flat=True))

    form=StudentForm(student_id=student_id)
    
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
         
        form = MarkForm(request.POST or None,request.FILES)  
        if form.is_valid():     
            student=form.save()
            return HttpResponse('Mark added')
        else:
            return HttpResponse("You already added the Mark")    
    
    
    return render(request, 'student.html', context={'student_form':form} )  

def login_user (request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.category=='teacher':

                return redirect('/student')   
                                     
            else:
                pk=user.id
                return redirect('/complete_data/{}'.format(pk))    
        else:
            messages.success(request,('Error logging in'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('/')

def student_data(request):
    
    import pdb;pdb.set_trace() 
    user=request.user
    teacher=user.teacher
    teacher_grade=Grade.objects.filter(teacher=teacher)
    # grade_id=list(teacher_grade.values_list('id',flat=True))
    # grade=Grade.objects.all()

    student=Student.objects.filter(grade__in=teacher_grade)
    
    

    student_id=list(student.values_list('user_id',flat=True))
    
    users = CustomUser.objects.filter(id__in=student_id)
    
    data=Mark.objects.filter(user__in=users)

    return render(request,'student_data.html',{'result':data})


def individualstudent_data(request):
    
    
    user=request.user
    teacher=user.teacher
    teacher_grade=Grade.objects.filter(teacher=teacher)
    grade_id=list(teacher_grade.values_list('id',flat=True))
    student=Student.objects.filter(grade_id__in=grade_id)
    student_id=list(student.values_list('user_id',flat=True))

    form=StudentDetailsForm(student_id=student_id)
    # import pdb;pdb.set_trace()


    if request.method == 'POST':
        # import pdb;pdb.set_trace()    
        form = SingleStudentForm(request.POST or None,request.FILES)
        # student_id=request.POST['user']
        # student=Mark.objects.filter(id=student_id)

        if form.is_valid():

            student_id=request.POST['user']
            user=Mark.objects.get(id=student_id)
            student=user.user
            id=student.id
            # data=form.save(commit=False) 
            # user= form.cleaned_data['user']
            
            return redirect('/complete_data/{}'.format(id))
           
    
    return render(request, 'individualstudent_data.html', context={'student_details':form})        

def complete_data(request,id):
    
    # import pdb;pdb.set_trace() 
    user = CustomUser.objects.get(id=id)
    data = Mark.objects.filter(user=user)
    if id != request.user.id and request.user.category != 'teacher':
        return HttpResponse('You cannot view what is not yours')



    
    return render(request, 'complete_data.html', {'mark': data})



def edit(request,id):

    # import pdb;pdb.set_trace()

    if id != request.user.id and request.user.category != 'teacher':
        return HttpResponse('You cannot Edit the marks')
    

    data=Mark.objects.get(id=id)

    
    form=StudentForm(request.POST or None,instance=data)
    
    if form.is_valid():

        form.save()

        message='mark updated'

        send_mail_to.delay(id,message)

    return render(request, 'edit.html', {'form': form})



def Student_field(request):

    form=StudentFieldForm
    if request.method=='POST':
        form = StudentFieldForm(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect("/success")

        
        form = StudentFieldForm()    
    return render(request, 'student_field.html', context={'student_field':form} )    

def teacher_field(request):
    import pdb;pdb.set_trace()
    form=TeacherForm
    if request.method=='POST':
        form = TeacherForm(request.POST or None)
        # import pdb;pdb.set_trace()
        if form.is_valid():

            data=form.save(commit=False)
            print('success')
            data.save()
            return redirect("/success")

        else:
            print(form.errors)
        form=TeacherForm()
            
    
    return render(request, 'teacher_field.html', context={'teacher_field':form} )  


def success(request):
    return render(request,'success.html',{})      
