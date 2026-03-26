from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello World")

def About(request):
    return HttpResponse("About Page")  

def contact(request):
    return HttpResponse("Contact Page")

def services(request):
    return HttpResponse("Services Page")