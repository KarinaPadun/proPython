from django.contrib.auth.models import User
from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=255)
    enrollments = models.ManyToManyField(User, through='members_app.UserEnrollment')

    def __str__(self):
        return self.title
