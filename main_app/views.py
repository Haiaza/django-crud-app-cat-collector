from django.shortcuts import render
from .models import Cat
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, './home/home.html')

def about(request):
    return render(request, 'about.html')

# class Cat:
#     # Init is important!  Every class usees these attributes to intstantiate
#     def __init__(self, name, breed, description, age):
#         self.breed = breed
#         self.name = name
#         self.description = description
#         self.age = age

#         # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html',{'cats':cats})