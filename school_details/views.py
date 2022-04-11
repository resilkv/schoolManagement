from django.shortcuts import  render, redirect,HttpResponse
from .forms import NewUserForm,StudentForm,StudentDetailsForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import CustomUser,Mark
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404






def register_request(request):
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()

    return render (request=request, template_name="register.html", context={"register_form":form})



def home(request):
    return render(request,'home.html')


def check_role_user(login_user):
    # import pdb;pdb.set_trace()   
    if login_user.is_authenticated and (login_user.category=='Teacher' or login_user.is_superuser):
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
            if user.category=='Teacher':

                return redirect('/student') 
                
                                                 
            else:
                return redirect('/')    
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

            # data.save()
            # data= form.cleaned_data.get("user")
            # data= form.cleaned_data.get("id")

            # data = request.GET['id_user']
            # id_user= form.cleaned_data['id_user']
            # print(data)
     
            # form.save()
            user= form.cleaned_data['user']
            # data = form.cleaned_data.get('id_user',None)
            # queryset=queryset.filter(user=user)
            # data=Mark.objects.filter(queryset)
            pk=user.id

            
            return redirect('/complete_data/{}'.format(pk))

            

    # form = StudentDetailsForm
    
    return render(request, 'indi_data.html', context={'student_details':form})        

def complete_data(request,pk):
    
    # import pdb;pdb.set_trace()
    data = Mark.objects.filter(pk=pk)
    # user = get_object_or_404(user, pk=id_user)
    return render(request, 'complete_data.html', {'user': data})


            


