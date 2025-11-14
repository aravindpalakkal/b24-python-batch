from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Course
import json

from myapp.serializers.course_serializer import CourseSerializer
from rest_framework.decorators import api_view

from django.shortcuts import render,redirect

@csrf_exempt
def create_course(request):
    try:

        course = request.POST['course']
        print(course)
        # course_instance = Course(course_name=course)
        # course_instance.save()
        Course.objects.create(course_name=course)
        return redirect('home')
        # return JsonResponse({'status':200, 'message':'course saved','course':course_instance.id})
    except Exception as e:
        print(e)
        # return JsonResponse({'status':400})

        return render(request,'dashboard.html')
    

def fn_getCourses(request):
    return render(request,'course_view.html')
    

def fetch_courses(request):
    try:
        if request.method == 'GET':
            if 'id' in request.GET:

                course_id = request.GET.get('cid')

                course = Course.objects.get(id=course_id)
                return render(request,'course_view.html',{'course':course})
            
            search_data = request.GET['search_data']
            courses = Course.objects.filter(course_name__istartswith=search_data)
            return render(request,'course_view.html',{'courseList':courses})
    
    except Exception as e:
        print(e)
        return render(request,'course_view.html',{'message':str(e)})
    

def getCourseById(courseId):
    try:
        course = Course.objects.get(id=courseId)
        return course
    
    except Course.DoesNotExist:
        return False
    
    except Exception as e:
        print(e)
        return JsonResponse( data= 'fail' ,status=400,safe=False)
    

@csrf_exempt
@api_view(['PUT'])
def updateCourse(request):
    try:
        req_data = request.data
        course_id = req_data['course_id']
        course = getCourseById(course_id)
        if not course:
            return JsonResponse(data=f'course does not exist with id {course_id}', status=200,safe=False)

        course.course_name = req_data['new_course_name']
        course.save()
        return JsonResponse(data=[course.id,course.course_name], status=200,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse( data= 'fail' ,status=400,safe=False)


@csrf_exempt
@api_view(['DELETE'])

def deleteCourse(request):
    try:
        req_data = request.data
        course_id = req_data['course_id']

        course = getCourseById(course_id)

        if not course:
            return JsonResponse(data='course does not exist',status=200,safe=False)
        
        course.delete()

        return JsonResponse(data='course deleted',status=200,safe=False)
    
    except Exception as e:
        print(e)
        return JsonResponse( data= 'fail' ,status=400,safe=False)