from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Lessonform(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ('subject','lesson_name','lesson_no','video','ppt','notes')




class LessonUpdateForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ('lesson_name','lesson_no','video','ppt','notes')