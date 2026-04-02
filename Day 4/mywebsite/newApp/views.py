from django.shortcuts import render

def NewApp(request):
    return render(request, 'newApp/products.html', {'active_page': 'products'})
