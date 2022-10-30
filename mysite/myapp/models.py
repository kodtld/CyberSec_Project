from email.policy import default
from platform import platform
from random import choices
from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200,default="Name of release")
    pub_date = models.DateField('date published',default="YYYY-MM-DD")
    platform = models.CharField(max_length=50,default="eg. Playstation")
    completion = models.CharField(max_length=50,default='0%')