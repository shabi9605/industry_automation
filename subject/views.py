from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Create your views here.

def view_subjects(request):
    try:
        user=StudentRegister.objects.get(user=request.user)
    except:
        pass
    try:
        user=TeacherRegister.objects.get(user=request.user)
    except:
        pass
    print(user.course.course_name)
    subjects=Subject.objects.filter(course=user.course)
    print(subjects)
    return render(request,'view_subjects.html',{'subjects':subjects})

def add_lesson(request):
    if request.method=="POST":
        lesson_add_form=Lessonform(request.POST,request.FILES)
        if lesson_add_form.is_valid():
            user=TeacherRegister.objects.get(user=request.user)
            print(user.course.course_name)
            cp=Lessons(user=request.user,course=user.course,subject=lesson_add_form.cleaned_data['subject'],lesson_name=lesson_add_form.cleaned_data['lesson_name'],lesson_no=lesson_add_form.cleaned_data['lesson_no'],video=lesson_add_form.cleaned_data['video'],ppt=lesson_add_form.cleaned_data['ppt'],notes=lesson_add_form.cleaned_data['notes'])
            cp.save()
            return render(request,'lesson_add_form.html',{'msg':'successfully added lesson'})
        else:
            return HttpResponse("Invalid form")
    lesson_add_form=Lessonform()
    return render(request,'lesson_add_form.html',{'form':lesson_add_form})


def view_lesson(request,subject_id):
    subject=Subject.objects.get(id=subject_id)
    lessons=Lessons.objects.filter(subject=subject)
    print(lessons)
    return render(request,'view_lessons.html',{'lessons':lessons})


def view_my_lessons(request):
    my_lessons=Lessons.objects.filter(user=request.user)
    print(my_lessons)
    return render(request,'view_my_lessons.html',{'my_lessons':my_lessons})


def update_lesson(request,lesson_id):
    lesson=Lessons.objects.get(id=lesson_id)
    lesson_update_form=LessonUpdateForm(instance=lesson)
    if request.method=="POST":
        lesson_update_form=LessonUpdateForm(request.POST,instance=lesson)
        lesson_update_form.save()
        return redirect('dashboard')
    return render(request,'lesson_update.html',{'form':lesson_update_form})








