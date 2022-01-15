from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.student_register,name='register'),
    path('teacher_register',views.teacher_register,name='teacher_register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('change_password',views.change_password,name='change_password'),
    path('view_profile',views.view_profile,name='view_profile'),
    path('complaint',views.complaint,name='complaint'),
    path('view_my_complaint',views.view_my_complaint,name='view_my_complaint'),
    path('view_payments',views.view_payments,name='view_payments'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)