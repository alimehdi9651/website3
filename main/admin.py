from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(recipe)
admin.site.register(Department)
admin.site.register(Student_ID)
admin.site.register(Student)
admin.site.register(Subject)

class SubjectMarkadmin(admin.ModelAdmin):
    list_display = ['student', 'subject','marks']


admin.site.register(Subject_mark, SubjectMarkadmin)