from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from . models import User

# Create your views here.



def fn_saveUser(request):
    try:
        if request.method == 'POST':


            name     = request.POST['name']
            mobile   = request.POST['mobile']
            password = request.POST['password']
            role     = request.POST['role']
        
            user_exist = User.objects.filter(mobile=mobile).exists()    

            if not user_exist:
                user = User.objects.create(name=name,username=mobile,mobile=mobile,password = password, roles=role)
                return HttpResponse(f'user saved... user ID is ..  {user.id}')
            
            return HttpResponse('user already exist...')
        
        else:
            return render(request,'register.html')
    
    except Exception as e:
        print(e)
        return HttpResponse(str(e))
    
    


def fn_login(request):
    if request.method == 'POST':

        try:
            username = request.POST.get('mobile')
            password = request.POST.get('pin')

            user = User.objects.get(mobile=username)

            if user.password == password:
                return redirect('home')
            else:
                return HttpResponse('login failed.. incorect username or password...!')
        
        except Exception as e:
            print(e)
            return HttpResponse('login failed.. incorect username or password...!')
    
    return render(request,'login.html')



def dashboard(req):
    return render(req,'dashboard.html')