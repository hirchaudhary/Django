from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages

def index(request):
    return render(request, 'user_name/index.html')

def adduser(request):
    check = Users.userManager.adduser(username=request.POST['username'])
    if check[0]:
        messages.add_message(request, messages.SUCCESS, "You have successfully added username!")
        return redirect('/success')
    else:
        for error in check[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
    return redirect('/')

def success(request):
    users = Users.userManager.all()
    context = {
        'users':users
    }
    return render(request, 'user_name/success.html', context)

def delete(request, id):
    Users.userManager.filter(id=id).delete()
    return redirect('/success')
