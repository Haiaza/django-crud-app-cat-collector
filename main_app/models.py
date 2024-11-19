from django.db import models
from django.urls import reverse
from django.utils.timezone import now

MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner")
)

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=1000) #textfields should be considered with 1000's
    age = models.IntegerField()

    def __str__(self): # so we have a useful namw when we callupon the cat class
        return self.name
    
    def get_absolute_url(self):
        return reverse('cat-detail',kwargs={'cat_id':self.id})

class Feeding(models.Model):
    date = models.DateField(default=now)
    meal = models.CharField(
        max_length=1, 
        choices=MEALS, 
        default=MEALS[0][0]
        )
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toy-detail',kwargs={'pk': self.id})