from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration(self, first_name, last_name, email, password, confirm_password):
        errors = []
        email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(first_name) < 2:
            errors.append("Enter valid first name")
        if len(last_name) < 2:
            errors.append("Enter valid last name")
        if not email_re.match(email):
            errors.append("Enter valid email")
        if len(password) < 8:
            errors.append("Enter valid password")
        if confirm_password != password:
            errors.append("Confirm password must be same as password")
        user = Users.userManager.filter(email=email)
        if user:
            errors.append('Email already exist')
        if len(errors) > 0:
            return False, errors
        else:
            #hashed = bcrypt.hashpw(str(password), bcrypt.gensalt())
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            print hashed
            return True, Users.userManager.create(first_name=first_name, last_name=last_name, email=email, password=hashed)

    def login(self, email, password):
        errors = []
        user = Users.userManager.filter(email=email)
        if not user:
            errors.append('Email does not exist')
        else:
            if bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return True, user[0].id, user[0].first_name
            else:
                errors.append('Password not match')
                
        if len(errors) > 0:
            return False, errors

class Users(models.Model):
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    email           = models.CharField(max_length=100)
    password        = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    userManager     = UserManager()
