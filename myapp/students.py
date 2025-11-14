


from django.shortcuts import render
from .models import User

# 7559079129

def fn_getUsers(request):

    try:
        print(request.GET)

        if 'id' in request.GET:
            user_id = request.GET.get('id')
            user = User.objects.get(id=user_id)
            # print(user.get_roles_display())
            return render(request,'student_view.html',context={'userData':user})
     
        
        else:
            if 'search-data' in request.GET:

                search_data = request.GET['search-data']
            
                name_list = User.objects.filter(name__istartswith=search_data).values_list('id','name')
                
                print(name_list)
            
                return render(request,'student_view.html',context={'nameList':name_list})
    
    except Exception as e:
        print(e)
    
    return render(request,'student_view.html')



