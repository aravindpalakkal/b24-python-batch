
from django.urls import path
from . import views,students,course

urlpatterns = [
    
    path('',views.fn_login,name='user-login'),
    
    path('home/',views.dashboard,name='home'),
    path('save-user/',views.fn_saveUser,name='save-user'),
    
    path('view-students/',students.fn_getUsers,name='search-students'),
    path('view-courses/',course.fn_getCourses,name='search-courses'),
    path("create-course/",course.create_course,name="saveCourse"),
    # path("get-all-courses/",course.fetch_courses,name='get-all-courses'),
    # # path('get-course/<int:courseId>',course.getCourseById,name='get-course'),
    # path('update-course/',course.updateCourse,name='update-course'),
    # path('delete-course/',course.deleteCourse,name='delete-course'),


    # path('create-user/',user.CreateUser.as_view(),name='create-user'),

]
