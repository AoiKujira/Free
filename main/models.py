from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField()
    second_day = models.IntegerField()

