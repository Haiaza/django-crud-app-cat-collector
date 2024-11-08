from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=1000) #textfields should be considered with 1000's
    age = models.IntegerField()

    def __str__(self): # so we have a useful namw when we callupon the cat class
        return self.name