from django.shortcuts import render

# importowanie odpowiedzi
from django.http import HttpResponse
from .models import *

# funkcje zwracające widoku

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = "Delivered").count()
    pending = orders.filter(status =  "Pending").count()


    context = {
        'orders':orders,
        'customers':customers,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
    }

    return render(request, 'myapp/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, "myapp/products.html", {'products':products})

def customer(request, pk):

    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        "customer":customer,
        "orders":orders,
        "order_count":order_count,
    }
    return render(request, "myapp/customer.html", context)