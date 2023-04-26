from django.shortcuts import render, redirect, get_object_or_404
from . import models, form

# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        information = ''
        username = request.user.id
        data = models.Passwords.objects.all().filter(creater=username)
        if data is not None:
            information = data
        
        return render(request, 'dashboard.html', {"entries": information})
    return redirect('login')

def newAdd(request):
    if request.user.is_authenticated:
        message = ''
        if request.method == 'POST':
            data = form.addPassword(request.POST)
            a = models.Passwords()
            
            
            message = data.errors
            if data.is_valid():

                newData = data.save(commit=False)
                newData.creater = request.user
                newData.save()

                return redirect('dashboard')

        return render(request, 'addNew.html', {'form': form.addPassword, 'message': message})
    return redirect('login')

def deleteEntery(request, del_id):
    if request.user.is_authenticated:
        models.Passwords.objects.filter(id=del_id).delete()
        return redirect('dashboard')
    else:
        return redirect('login')

def updateEntery(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(models.Passwords, id=id, creater=request.user.id)
        myform = form.addPassword(instance=data)

        if request.method == 'POST':
            myform = form.addPassword(request.POST, instance=data)

            if myform.is_valid():
                new = myform.save(commit=False)
                new.creater = request.user
                
                myform.save()

                return redirect('dashboard')


        
        return render(request, 'update.html', {'form': myform, 'message': '', 'id':id})
    else:
        return redirect('login')