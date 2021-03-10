from django.shortcuts import render, redirect

# importowanie odpowiedzi
from django.http import HttpResponse
from .models import *
from .forms import *

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



def createOrder(request):

    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}

    return render(request, 'myapp/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}

    return render(request, 'myapp/order_form.html', context)


def deleteOrder(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {"item":item}
    return render(request, "myapp/delete.html", context)