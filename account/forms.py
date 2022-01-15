from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    
    class Meta:
        model=User
        fields=('username','password1','password2','email')

class ProfileForm(forms.ModelForm):
    address=forms.Textarea()
    class Meta:
        model=StudentRegister
        fields=('phone','image','course','address')


class TeacherForm(forms.ModelForm):
    class Meta:
        model=TeacherRegister
        fields=('phone','image','course','certificate','address')

class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    first_name=forms.CharField(help_text=None,label='firstname')
    last_name=forms.CharField(help_text=None,label='lastname')
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')

class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model=StudentRegister
        fields=('address','phone','image')



class ComplaintForm(forms.ModelForm):
    complaint=forms.Textarea()
    class Meta:
        model=Complaint
        fields=('complaint',)


