from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Mark,Subject
from .models import CustomUser





class NewUserForm(UserCreationForm):  
    
    email = forms.EmailField()
    
    


    class Meta:
        model = CustomUser
        password1 = forms.CharField(widget=forms.PasswordInput)
        password2= forms.CharField(widget=forms.PasswordInput)
        fields = ('username', 'email', 'password1' ,'password2','category' )

        help_texts = {
            'username': None,
        }

       
        def clean(self):
            cd = self.cleaned_data
            if cd.get('password1') != cd.get('password2'):
                self.add_error('password2', "passwords do not match !")
            return cd


        def clean_password(self):
            if self.data['password1'] != self.data['password2']:
                raise forms.ValidationError('Passwords are not the same')
            return self.data['password1']    



    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.category=self.cleaned_data['category']
        if commit:
            user.save()
        return user

class StudentForm(forms.ModelForm):
    

    class Meta:
        model = Mark
        fields = '__all__'


class StudentDetailsForm(forms.ModelForm):

    
    class Meta:
        model = Mark
        fields = ('user',)


  

