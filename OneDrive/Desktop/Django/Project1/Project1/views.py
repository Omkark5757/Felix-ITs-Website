from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')  # Better to use templates than raw text

def placement(request):
    return render(request, 'placement.html')

def contact(request):
    return render(request, 'contact.html')

def felix_form(request):
    return render(request, 'felix_form.html')


