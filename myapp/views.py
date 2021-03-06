from django.shortcuts import render

# importowanie odpowiedzi
from django.http import HttpResponse

# funkcje zwracające widoku

def home(request):
    return render(request, 'myapp/dashboard.html')

def products(request):
    return render(request, "myapp/products.html")

def customer(request):
    return render(request, "myapp/customer.html")