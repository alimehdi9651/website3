from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(recipe)
admin.site.register(Department)
admin.site.register(Student_ID)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Subject_mark)