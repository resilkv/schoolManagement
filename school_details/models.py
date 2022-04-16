
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime



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

GRADE= (
	(5,'5'),
	(6,'6'),
	(7,'7'))

class Grade(models.Model):

	grade=models.IntegerField(choices=GRADE,default='5')

	def __str__(self):
		return self.grade.__str__()		

class Student(models.Model):
	guardian=models.CharField(max_length=50)
	dob=models.DateField()
	address=models.TextField(max_length=200)
	grade=models.OneToOneField('Grade',on_delete=models.CASCADE)


class Teacher(models.Model):
	address=models.TextField(max_length=200)
	teaching_in=models.ForeignKey('Grade',on_delete=models.CASCADE)
	dob=models.DateField()




	

