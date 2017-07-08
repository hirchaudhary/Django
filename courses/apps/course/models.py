from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def addCourse(self, name, description):
        errors = []
        if len(name) < 1:
            errors.append("Name can't be empty")
        if len(description) < 1:
            errors.append("Description can't be empty")
        if len(errors) > 0:
            return False, errors
        else:
            return True, Courses.courseManager.create(name=name, description=description)

class Courses(models.Model):
    name   = models.CharField(max_length=255)
    description  = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    courseManager = CourseManager()
