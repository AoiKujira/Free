from django.contrib.auth.models import User
from django.db import models

WEEKDAY_CHOICES = [
    (0, 'شنبه'),
    (1, 'یک‌شنبه'),
    (2, 'دوشنبه'),
    (3, 'سه‌شنبه'),
    (4, 'چهارشنبه'),
]


class Course(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=WEEKDAY_CHOICES)
    second_day = models.IntegerField(blank=True, null=True, choices=WEEKDAY_CHOICES)
