from django.shortcuts import render
from .models import Cat
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
