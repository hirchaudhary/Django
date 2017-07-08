from django.shortcuts import render

def index(request):
    return render(request, 'dis_ninja/index.html')

def ninjas(request):
    return render(request, 'dis_ninja/ninjas.html')

def color(request, color):
    context = {
        'color': color
    }
    return render(request, 'dis_ninja/color.html', context)
