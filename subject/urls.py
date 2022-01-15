from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('view_subjects',views.view_subjects,name='view_subjects'),
    path('add_lesson',views.add_lesson,name='add_lesson'),
    path('view_lesson/<int:subject_id>',views.view_lesson,name='view_lesson'),
    path('view_my_lessons',views.view_my_lessons,name='view_my_lessons'),
    path('update_lesson/<int:lesson_id>',views.update_lesson,name='update_lesson'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)