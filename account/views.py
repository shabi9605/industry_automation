from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . forms import *
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# from teacher.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from payment.models import *

 

# Create your views here.

def index(request):
    return render(request,'home.html')

def student_register(request):
    reg=False
    
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            
            profile.save()
            
            messages.success(request,'Registration successfully completed you  can login now')
            reg=True
            return HttpResponseRedirect('user_login')
        else:
            
            HttpResponse("Invalid Form")
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
    return render(request,'register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})



def teacher_register(request):
    reg=False
    
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=TeacherForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            
            profile.save()
            
            messages.success(request,'Registration successfully completed you  can login now')
            reg=True
            return HttpResponseRedirect('user_login')
        else:
            
            HttpResponse("Invalid Form")
    else:
        user_form=UserForm()
        profile_form=TeacherForm()
    return render(request,'teacher_register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(list)
        try:
            user1=StudentRegister.objects.get(user=user)
        except:
            pass

        try:
            user2=TeacherRegister.objects.get(user=user)
            print(user1)
        except:
            pass

        if user:
            if user.is_active:
                try:
                    if user1:
                        active=StudentRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if user2:
                        active=TeacherRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass
                
                try:
                    if user.is_superuser:
                        
                        login(request,user)
                
                
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass
            else:
                return HttpResponse("Not active")       
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request,'home.html')

def dashboard(request):
    payment=Payment.objects.filter(user=request.user,paid=True)
    return render(request,'dashboard/dashboard.html',{'payment':payment})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

# def allsubject(request):
#     User_instance=request.user.id
#     print(User_instance)
#     courses=Subject.objects.filter(course__user__id=User_instance)
#     print(courses)
    #   return render(request,'allsubject.html',{'courses':courses})

    
    
def update_profile(request):

    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        try:
            update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.studentregister)
        except:
            pass

        try:
            update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.teacherregister)
        except:
            pass

        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        try:
            update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.studentregister)
        except:
            pass

        try:
            update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.teacherregister)
        except:
            pass
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_profile.html',context)



def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCESSFULLY UPDATED")
            return render(request,'change_password.html')
        else:
            messages.error(request,"PLEASE CORRECT ERROR")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{"form":form})



def view_profile(request):
    try:
        user=StudentRegister.objects.get(user=request.user)
    except:
        pass
    try:
        user=TeacherRegister.objects.get(user=request.user)
    except:
        pass
    print(user)
    return render(request,'view_profile.html',{'user':user})


def complaint(request):
    if request.method=="POST":
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
            cp=Complaint(user=request.user,complaint=complaint_form.cleaned_data['complaint'])
            cp.save()
            return render(request,'add_complaint.html',{'msg':'successfully added complaint'})
        else:
            return HttpResponse("Invalid form")
    complaint_form=ComplaintForm()
    return render(request,'add_complaint.html',{'form':complaint_form})


def view_my_complaint(request):
    my_complaints=Complaint.objects.filter(user=request.user)
    return render(request,'my_complaints.html',{'my_complaints':my_complaints})


def view_payments(request):
    payments=Payment.objects.all().order_by('-id')
    return render(request,'view_payments.html',{'payments':payments})




