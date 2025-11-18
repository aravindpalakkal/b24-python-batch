from django.contrib import admin

# Register your models here.

from . models import Course,User,UserRole

admin.site.register(Course)

admin.site.register(User)
admin.site.register(UserRole)