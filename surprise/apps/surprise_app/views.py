from django.shortcuts import render
import random
values = ['Video Game', 'Tour', 'Ring', 'Dance', 'Song', 'No surprise here', 'Garden', 'Ice cream', 'Chocolate', 'Watch', 'TV', 'Fan']
def index(request):
    return render(request, 'surprise_app/index.html')

def guess(request):
    num = int(request.POST['guess'])
    items = []
    random.shuffle(values)
    for i in range(0,num):
        items.append(values[i])
    context = {
        'items': items
    }
    print context
    return render(request, 'surprise_app/result.html', context)
