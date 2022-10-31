from telnetlib import GA
from django.contrib import admin

# Register your models here.

from .models import Game
admin.site.register(Game)