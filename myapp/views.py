from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from . models import User,UserRole

from django.contrib.auth import authenticate,login,logout

# Create your views here.

def fn_saveUser(request):
    try:
        if request.method == 'POST':


            name     = request.POST['name']
            mobile   = request.POST['mobile']
            password = request.POST['password']
            role_id     = request.POST['role'] ### role id from api
        
            user_exist = User.objects.filter(mobile=mobile).exists()
            
            role = UserRole.objects.get(id=role_id)


            if not user_exist:
                user = User.objects.create(name=name,username=mobile,mobile=mobile,password = password, fk_role=role,is_active=False)
                user.set_password(password)
                user.save()
                return HttpResponse(f'user saved... user ID is ..  {user.id}')
            
            return HttpResponse('user already exist...')
        
        else:
            # roles = [{'key':key,'value':value} for key,value in User.ROLE_CHOICES]
            roles = UserRole.objects.all()
            print(roles)
            return render(request,'register.html',{'roles':roles})
    
    except Exception as e:
        print(e)
        return HttpResponse(str(e))
    
    


def fn_login(request):
    if request.method == 'POST':

        try:
            username = request.POST.get('mobile')
            password = request.POST.get('pin')

            user = authenticate(request,username=username,password=password)
            # print(user)
            if user:
                login(request,user)
                # print(request.user.is_authenticated)
                # print(request.user.roles)
                return redirect('home')
                               
            else:
                return render(request,'login.html',{'message':'login failed.. permission denied or incorect username or password...!'})
                
        
        except Exception as e:
            print(e)
            return render(request,'login.html',{'message':'login failed.. incorect username or password...!'})
                
    
    return render(request,'login.html')



def dashboard(req):
    return render(req,'dashboard.html')


def user_logout(request):
    logout(request)