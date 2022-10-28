from django.shortcuts import render
# from django.http import HttpResponse
from .models import Motorcicle
from .models import Albert

# Create your views here.

def home(request):
    motorcicles = Motorcicle.objects.all()
    return render(request, 'home.html', {'motorcicles': motorcicles})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    albert = Albert.objects.all()
    return render(request, 'contacts.html', {'albert': albert})

