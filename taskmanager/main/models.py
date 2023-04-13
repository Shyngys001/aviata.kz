from django.db import models
from django.urls import reverse


# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=55)
    task = models.TextField('Описания')

    def __str__(self):
        return self.title


class Tasks(models.Model):
    titles = models.CharField('Название', max_length=55)
    tasks = models.TextField('Описания')

    def __str__(self):
        return self.titles