
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.conf import settings
from django.utils.timezone import now



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
	date_submit=models.DateTimeField(auto_now=True, editable=False)


	class Meta:
    		unique_together = ('user','subject')
    		


	
	
	def __str__(self):

		return self.user.__str__() 


	@property
	def result(self):
		# import pdb;pdb.set_trace()

		if self.mark>=50:
			return 'pass'
		else:
			return 'fail'	


		

class Student(models.Model):
	user=models.OneToOneField('CustomUser',on_delete=models.CASCADE,default=None)
	guardian=models.CharField(max_length=50)
	dob=models.DateField()
	address=models.TextField(max_length=200)
	grade=models.ForeignKey('Grade',on_delete=models.CASCADE,default=5)
	

	def __str__(self):
		return self.user.__str__()


	




class Teacher(models.Model):
	user=models.OneToOneField('CustomUser',on_delete=models.CASCADE,default=None)
	address=models.TextField(max_length=200)
	dob=models.DateField()
	
	def __str__(self):
		return self.user.__str__()

		

GRADE= (
	(5,'5'),
	(6,'6'),
	(7,'7'))

class Grade(models.Model):

	grade=models.IntegerField(choices=GRADE,default='5')
	teacher=models.ForeignKey('Teacher',on_delete=models.CASCADE,default=5)
	
	def __str__(self):
		return self.grade.__str__()



	

