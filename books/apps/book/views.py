from django.shortcuts import render
from .models import Books
def index(request):
    #Books.objects.create(title='Veronika decides to die',author='Paulo Coelho', published_date='1998-12-02',category='thriller')
    book = Books.objects.get(id=2)
    print book.title, book.author
    books = Books.objects.raw('SELECT * FROM book_books')
    print books
    for book in books:
        print book.title
    return render(request, 'book/index.html')
