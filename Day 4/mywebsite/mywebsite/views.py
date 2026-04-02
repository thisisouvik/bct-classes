from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'index.html', {'active_page': 'home'})

def About(request):
    return HttpResponse("About Page")  

def contact(request):
    return HttpResponse("Contact Page")

def services(request):
    return HttpResponse("Services Page")