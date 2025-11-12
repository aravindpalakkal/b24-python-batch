from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin


# Create your models here.


class User(AbstractUser,PermissionsMixin):
    ROLE_CHOICES = (
        ('stud','Student'),
        ('ad','admin')
    )
    name      = models.CharField(max_length=50)
    mobile    = models.CharField(max_length=12,unique=True)
    roles     = models.CharField(max_length=10,choices=ROLE_CHOICES)


class Course(models.Model):
    course_name = models.CharField(max_length=50)


class Student(models.Model):
    fk_user   = models.OneToOneField(User,on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course,on_delete=models.CASCADE)