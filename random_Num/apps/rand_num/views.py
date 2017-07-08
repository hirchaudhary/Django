from django.shortcuts import render, redirect
import random
import string
def index(request):
    try:
        request.session['attempt'] += 1
    except:
        request.session['attempt'] = 1
    return render(request, 'rand_num/index.html')

def randnum(request):
    ranstr = ""
    string = "ABCDEFGHIJKLMONPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
    for i in range(1,15):
        ranstr += string[random.randrange(0,52)]
    request.session['ranstr'] = ranstr
    return redirect('/')
