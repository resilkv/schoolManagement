
from django.db import models
from django.contrib.auth.models import AbstractUser



CATEGORY_CHOICES = (
    ('teacher','Teacher'),
    ('student', 'Student'))
    



class CustomUser(AbstractUser):
	email=models.EmailField(max_length=100,unique=True)
	category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Teacher')
	
	



class Subject(models.Model):
	
	name = models.CharField(max_length=50)

	def __str__(self):
		
		return self.name
	


class Mark(models.Model):
	user=models.ForeignKey('CustomUser',on_delete= models.CASCADE,related_name='user_set')
	subject=models.ForeignKey('Subject',on_delete= models.CASCADE,related_name='name_set')
	mark=models.IntegerField()

	
	def __str__(self):
		return self.user.__str__() 
