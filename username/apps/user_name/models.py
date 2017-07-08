from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def adduser(self, username):
        errors = []
        user = Users.userManager.filter(username=username)
        if user:
            errors.append('Username already exist')

        if len(username) < 8 or len(username) > 26:
            errors.append('Username is not in range')

        email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_re.match(username):
            errors.append('Username is not valid')

        if len(errors) > 0:
            return False, errors
        else:
            return True, Users.userManager.create(username=username)

class Users(models.Model):
    username    = models.CharField(max_length=26)
    created_at  = models.DateTimeField(auto_now_add=True)
    userManager = UserManager()
