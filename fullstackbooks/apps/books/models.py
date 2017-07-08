from __future__ import unicode_literals

from django.db import models

class BooksManager(models.Manager):
    def addbook(self, title, author, category):
        errors = []
        if len(title) < 1:
            errors.append("Title can't be empty")
        if len(author) < 1:
            errors.append("Author can't be empty")
        if len(category) < 1:
            errors.append("Category can't be empty")
        if len(errors) > 0:
            return False, errors
        else:
            return True, Books.booksManager.create(title=title, author=author, category=category)

class Books(models.Model):
    title   = models.CharField(max_length=255)
    author  = models.CharField(max_length=255)
    category= models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    booksManager = BooksManager()
