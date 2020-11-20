from django.db import models
from django.urls import reverse

class Task(models.Model):
    description = models.CharField(max_length=200)
    time = models.IntegerField()
    person = models.CharField(max_length=100)

    def __str__(self):
        return self.description