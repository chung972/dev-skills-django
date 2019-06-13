from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')
    # like how render behaves in express, render in django also looks for
    # files RELATIVE to the templates directory