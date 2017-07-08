from django.shortcuts import render, redirect
from .models import Books
from django.contrib import messages

def index(request):
    books = Books.booksManager.all()
    context = {
        'books': books
    }
    return render(request, 'books/index.html', context)

def addbook(request):
    check = Books.booksManager.addbook(request.POST['title'], request.POST['author'], request.POST['category'])
    if not check[0]:
        for error in check[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')
