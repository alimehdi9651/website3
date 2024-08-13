from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class recipe(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null=True)
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_img = models.ImageField()

    

class Department(models.Model):
    department = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']


class Student_ID(models.Model):
    student_id = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name = "depart", on_delete = models.CASCADE)
    student_id = models.OneToOneField(Student_ID, related_name = "stu_id", on_delete = models.CASCADE)
    student_name= models.CharField(max_length = 100)
    student_email = models.EmailField(unique = True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    

    class Meta():
        ordering = ['student_name']
        verbose_name = "student"

        

    
