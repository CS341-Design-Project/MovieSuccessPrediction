from django.db import models

# Create your models here.

class Director(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.code,self.name,self.rating)

class Producer(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.code,self.name,self.rating)

class Narrative(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.code,self.name,self.rating)

class Hero(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.code,self.name,self.rating)

class Actor(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.code,self.name,self.rating)

class Song(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.code,self.name,self.rating)
