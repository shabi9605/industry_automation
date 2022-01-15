from django.contrib import admin
from .models import *
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=('user','course','status')

admin.site.register(StudentRegister,RegisterAdmin)

admin.site.register(Course)
admin.site.register(Complaint)
admin.site.register(TeacherRegister)