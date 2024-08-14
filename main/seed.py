from faker import Faker
fake = Faker()
import random 
from .models import *


def create_student_marks(n=100):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                Subject_mark.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(30,99)
                )
    except Exception as e:
        print(e)



def seed_db(n=10):
    try:
        for i in range(n):
             department_objs = Department.objects.all()
             rand_idx = random.randint(0, len(department_objs)-1)
             department = department_objs[rand_idx]
             student_name = fake.name()
             student_age = random.randint(19,26)
             student_id = f'STU-0{random.randint(100, 999)}'
             student_email = fake.email()
             student_id_obj = Student_ID.objects.create(student_id = student_id)
             student_address = fake.address()

             student_obj = Student.objects.create(
                 department = department,
                 student_age = student_age,
                 student_email=student_email,
                  student_id = student_id_obj,
                 student_name = student_name,
                 student_address = student_address,
                 )
             
    except Exception as e:
        print(e)
        



