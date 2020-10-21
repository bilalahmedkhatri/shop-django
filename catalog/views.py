from django.shortcuts import render
from . models import Item, OrderItem, Order
# Create your views here.


def home(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "home.html", context)


def product(request):
    context = {
        "orderitem": OrderItem.objects.all()
    }
    return render(request, "product.html", context)


def checkout(request):
    context = {
        "order": Order.objects.all()        
    }
    return render(request, "checkout.html")

# def (request):
