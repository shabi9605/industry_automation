
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    course_name=models.CharField(max_length=50)
    description=models.CharField(max_length=20)
    course_image=models.ImageField(upload_to="course_image",default="default.png")
    def __str__(self):
        return str(self.course_name)


class StudentRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default='Mathematics')
    address=models.TextField(blank=True,null=True)
    phone=PhoneNumberField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    status=models.BooleanField(default=False)
    
    
    
    paid=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class TeacherRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default='Mathematics')
    address=models.TextField(blank=True,null=True)
    phone=PhoneNumberField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    status=models.BooleanField(default=False)
    certificate=models.FileField(upload_to='certificate',null=True,blank=True)
    def __str__(self):
        return str(self.user.username)


class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.TextField()
    def __str__(self):
        return str(self.user.username)
