from django.shortcuts import render, redirect

def index(request):
    return render(request, 'landscape_app/index.html')

def show(request, num):
    context = {
        'number': int(num)
    }
    if num > 0 or num < 51:
        return render(request, 'landscape_app/landscape.html', context)
    return redirect('/')
