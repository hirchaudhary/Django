from django.shortcuts import render
from .models import Users, Messages, Comments
def index(request):
    user = Users.objects.all()
    print user
    return render(request, 'the_wall/index.html')
