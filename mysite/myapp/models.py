from email.policy import default
from platform import platform
from random import choices
from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    platform = models.CharField(max_length=50)
    completion = models.CharField(max_length=50,default='0%')