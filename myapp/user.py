
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from . models import User
import json

# class CreateUser(APIView):

#     def get(self,request):
#         try:
#             roles = [{'key':key,'value':value} for key,value in User.ROLE_CHOICES]
#             print(roles)
#             return Response(data=roles,status=status.HTTP_200_OK)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def post(self,request):
#         try:
#             data = request.data
#             print(data)
#             name = data['name']
#             mobile = data['mobile']
#             password = data['password']
#             role = data['role']
            
#             if role == 'ad':
#                 user = self._saveAdmin(name,mobile,password,role)
            
#             else:
#                 user = self._saveStudent(name.mobile,password,role)
        

#             return Response(data=user,status=status.HTTP_201_CREATED)
        
#         except Exception as e:
#             print(e)
#             return Response(data=str(e),status=status.HTTP_400_BAD_REQUEST)

#     def _saveAdmin(self,name,mobile,password,role):
#         admin = User(name=name,mobile=mobile,username=mobile,roles=role)
#         admin.set_password(password)
#         admin.save()
#         return admin.id
        
    
#     def _saveStudent(self,name,mobile,password,role):
#         student = User(name=name,mobile=mobile,roles=role)
#         student.set_password(password)
#         student.save()
#         return student.id




    

def updateUserStatus(request):
    try:
        if request.method == 'POST':
            reqData = json.loads(request.body)
            print(reqData)

            user_id = reqData.get('user_id')
            
            user = User.objects.get(id=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            
            # print(user.is_active)

            user.save() 
            print(user_id)
            return JsonResponse({'message':'status updated...'})
    
    except Exception as e:
        print(e)
        return JsonResponse({'message':'status updation failed... str(e)'})