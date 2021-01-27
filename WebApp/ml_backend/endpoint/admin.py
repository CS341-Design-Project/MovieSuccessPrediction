from django.contrib import admin
from .models import Director, Producer, Narrative, Hero, Actor, Song
# Register your models here.

admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(Narrative)
admin.site.register(Hero)
admin.site.register(Actor)
admin.site.register(Song)