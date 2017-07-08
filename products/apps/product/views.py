from django.shortcuts import render
from .models import Products
def index(request):
    Products.objects.create(name='car', description='this car could take you anywhere with the maximum speed you are able to go on', weight=1000, price=20000, cost=18000, category='cars')
    product = Products.objects.all()
    print product
    return render(request, 'product/index.html')
