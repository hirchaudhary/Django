from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_app/index.html')

def process(request, place):

    if place == "farm":
        gold = random.randrange(10,20)
        message = "You earned {} gold at the farm! {}".format(gold,datetime.strftime(datetime.now(),'%H:%M:%S %m/%d/%Y'))
    elif place == "cave":
        gold = random.randrange(1,10)
        message = "You earned {} gold in the cave! {}".format(gold,datetime.strftime(datetime.now(),'%H:%M:%S %m/%d/%Y'))
    elif place == "house":
        gold = random.randrange(20,30)
        message = "You earned {} gold in the house! {}".format(gold,datetime.strftime(datetime.now(),'%H:%M:%S %m/%d/%Y'))
    elif place == "casino":
        gold = random.randrange(-50,50)
        if gold < 0:
            message = "You lost {} gold at the casino! {}".format(gold,datetime.strftime(datetime.now(),'%H:%M:%S %m/%d/%Y'))
        elif gold > 0:
            message = "You won {} gold at the casino! {}".format(gold,datetime.strftime(datetime.now(),'%H:%M:%S %m/%d/%Y'))
        else:
            message = "You neither lost nor made money at the casino!".format(gold)
    request.session['gold'] += gold
    request.session['activities'].append(message)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
