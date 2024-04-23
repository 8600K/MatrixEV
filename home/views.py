from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

# About Us
def about(request):
    return render(request, 'pages/about.html')

# Responsible Gambling
def rg(request): 
    return render(request, 'pages/responsible-gaming.html')

def wip(request):
    return render(request, 'pages/work-in-progress.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

