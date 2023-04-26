from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def create_user(request):
    message = ''
    if not request.user.is_authenticated:
        if request.method == 'POST':
            data = forms.newUser(request.POST)
            message = data.errors
            
            if data.is_valid():
                data.save(commit=False)
                data.creater_id = request.user.id
                data.save()
                return redirect('login')
        
        return render(request, 'signup.html', {'form': forms.newUser, 'message': message})
    else:
        return redirect('dashboard')


def login_(request):
    message = ''
    if not request.user.is_authenticated:
        if request.method == "POST":
            data = forms.Login(request.POST)
            if data.is_valid():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                    
                    
                else:
                    message = 'invalid Details'
            
        return render(request, "login.html", {'form': forms.Login, 'message': message})
    
    else: 
        return redirect('dashboard')



def logout_(request):
    logout(request)
    return redirect('login')
