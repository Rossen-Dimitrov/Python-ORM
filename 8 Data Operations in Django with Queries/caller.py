import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student
from datetime import datetime


# Import your models
# Create and check models
# Run and print your queries


def add_students():
    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date=datetime.strptime('15/05/1995', '%d/%m/%Y').strftime('%Y-%m-%d'),
        email='john.doe@university.com'
    )
    Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        birth_date=None,
        email='jane.smith@university.com'
    )
    stud_1 = Student(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date=datetime.strptime('10/02/1998', '%d/%m/%Y').strftime('%Y-%m-%d'),
        email='alice.johnson@university.com'
    )
    stud_1.save()

    stud_2 = Student(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date=datetime.strptime('25/11/1996', '%d/%m/%Y').strftime('%Y-%m-%d'),
        email='bob.wilson@university.com'
    )
    stud_2.save()


# add_students()
# print(Student.objects.all())

def get_students_info():
    students_list = []
    for student in Student.objects.all():
        students_list.append(
            f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}"
        )
    return '\n'.join(students_list)


print(get_students_info())

