from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages

def index(request):
    return render(request, 'login_reg/index.html')

def success(request):
    return render(request, 'login_reg/success.html')

def registration(request):
    check = Users.userManager.registration(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], confirm_password=request.POST['confirm_password'])

    if check[0]:
        messages.add_message(request, messages.SUCCESS, "You have successfully registerd!")
        request.session['id'] = check[1].id
        request.session['first_name'] = check[1].first_name
        return redirect('/success')
    else:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    return redirect('/')

def login(request):
    check = Users.userManager.login(email=request.POST['email'], password=request.POST['password'])

    if check[0]:
        messages.add_message(request, messages.SUCCESS, "You have successfully logged in!")
        request.session['id'] = check[1]
        request.session['first_name'] = check[2]
        return redirect('/success')
    else:
        for error in check[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
    return redirect('/')
