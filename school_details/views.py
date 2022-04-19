from django.shortcuts import  render, redirect,HttpResponse
from .forms import NewUserForm,StudentForm,StudentDetailsForm,StudentField,TeacherField
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import CustomUser,Mark,Grade,Student,Teacher
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden






def register_request(request):
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        # import pdb;pdb.set_trace()
        if form.is_valid():

            user = form.save()
            
            messages.success(request, "Registration successful." )

            if user.category=='student':
                form=StudentField
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
    # import pdb;pdb.set_trace()   
    if login_user.is_authenticated and (login_user.category=='teacher' or login_user.is_superuser):
        return True
    else:
        return False 

 
@login_required(login_url=None)
@user_passes_test(check_role_user,login_url='/')
def student_details(request):
    form=StudentForm
    # import pdb;pdb.set_trace()   
    if request.method == 'POST':
        form = StudentForm(request.POST)  
        if form.is_valid():     
            studet=form.save()
            # return redirect('')



    form = StudentForm()
    

    
    return render(request, 'student.html', context={'student_form':form} )  




def login_user (request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # import pdb;pdb.set_trace()
            
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
    data = Mark.objects.all()


    # data = Mark.objects.filter(pk=id)
    return render(request,'student_data.html',{'result':data})



def indi_data(request):
    form=StudentDetailsForm
      
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST or None)
        # import pdb;pdb.set_trace()  
        if form.is_valid():
            # import pdb;pdb.set_trace()
            data=form.save(commit=False)
            # data=form.cleaned_data.get('user')
            # data=Mark.objects.get(pk=request.user)

            
     
            # form.save()
            user= form.cleaned_data['user']
            
            id=user.id
                    
            return redirect('/complete_data/{}'.format(id))

            

    
    
    return render(request, 'indi_data.html', context={'student_details':form})        

def complete_data(request,id):
    
    # import pdb;pdb.set_trace() 
    user = CustomUser.objects.get(id=id)
    data = Mark.objects.filter(user=user)
    if id != request.user.id and request.user.category != 'teacher':
        return HttpResponse('You cannot view what is not yours')


    
   
    return render(request, 'complete_data.html', {'user': data})


def Student_field(request):

    form=StudentField
    if request.method=='POST':
        form = StudentField(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect("/success")

        
        form = StudentField()
    

    
    return render(request, 'student_field.html', context={'student_field':form} )    

def teacher_field(request):

    form=TeacherField
    if request.method=='POST':
        form = TeacherField(request.POST or None)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            data=form.save(commit=False)
            print('success')
            data.save()
            return redirect("/success")

        else:
            print(form.errors)    

        
    
        form=TeacherField()    
    
    return render(request, 'teacher_field.html', context={'teacher_field':form} )  


def success(request):
    return render(request,'success.html',{})      
    

