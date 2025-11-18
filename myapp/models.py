from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserRole(models.Model):
    role = models.CharField(max_length=10)

class User(AbstractUser):
   
    name      = models.CharField(max_length=50)
    mobile    = models.CharField(max_length=12,unique=True)
    fk_role   = models.ForeignKey(UserRole,on_delete=models.CASCADE,null=True,default=None)
    


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    amount      = models.IntegerField(default=0)
    fk_user     =  models.ManyToManyField(User,blank=True)


