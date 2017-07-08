from django.shortcuts import render, redirect
from .models import Courses
from django.contrib import messages

def index(request):
    courses = Courses.courseManager.all()
    context = {
        'courses': courses
    }
    return render(request, 'course/index.html', context)

def addCourse(request):
    check = Courses.courseManager.addCourse(request.POST['name'], request.POST['description'])
    if not check[0]:
        for error in check[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def delete(request, id):
    courses = Courses.courseManager.filter(id=id)
    context = {
        'courses': courses
    }
    request.session['id'] = id
    return render(request, 'course/confirm.html', context)

def confirm(request, id):
    Courses.courseManager.filter(id=id).delete()
    return redirect('/')
