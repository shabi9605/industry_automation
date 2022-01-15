from django.db import models
from django.template.defaultfilters import date, slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os
from django.urls import reverse
from account.models import *
from django.utils import timezone

# Create your models here.
class Subject(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default='Mathematics')
    name=models.CharField(max_length=50)
    
    description=models.TextField()
    def __str__(self):
        return str(self.name)

class Lessons(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)
    lesson_name=models.CharField(max_length=50)
    lesson_no=models.IntegerField()
    video=models.FileField(upload_to='videos')
    ppt=models.FileField(upload_to='ppt')
    notes=models.FileField(upload_to='notes')
    def __str__(self):
        return str(self.lesson_name)



