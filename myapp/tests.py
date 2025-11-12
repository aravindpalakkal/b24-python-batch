from django.test import TestCase
from django.urls import reverse
from . models import Course
# Create your tests here.

class MyTest(TestCase):
    def setUp(self):
        self.course = {"course":"python-django"}
    

    def test_add(self):
        url = reverse('saveCourse')
        response = self.client.post(url,self.course)
        self.assertEqual(response.status_code,200)
       
        self.assertEqual(Course.objects.count(),1)