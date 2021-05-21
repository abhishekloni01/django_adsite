from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'User - {username} successfully logged in')
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials! Please use valid username and password')
            return redirect('/accounts/login')
        
    else:
         return render(request,'login.html')

        
   
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('in if')
                messages.info(request,'Username is already taken!')
                return redirect('register')
            else:
                print('in else ------------------------')
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password1)
                user.save()
                messages.success(request,f'Successfully registered with username - {username}! Now you can login')
                return redirect('loginUser')

        else:
            messages.info(request,'Password is not matching!')
            return redirect('register')
    else:
        return render(request,'register.html')


def logoutUser(request):
    logout(request)
    return redirect('/')





