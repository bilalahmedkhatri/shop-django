from django.shortcuts import render
from . models import Item, OrderItem, Order, SliderItem
from django.views.generic import ListView, DetailView
# Create your views here.


class HomeView(ListView):
    model = Item
    # model = SliderItem
    template_name = "home.html"

# def home(request):
#     context = {
#         "items": Item.objects.all(),
#         "slider": SliderItem.objects.all()
#     } 
#     return render(request, "home.html", context)


class ItemDetailView(DetailView):
    model = Order
    template_name = "product.html"

# def product(request):
#     context = {
#         "Item": Order.objects.all()
#     }
#     return render(request, "product.html", context)


def checkout(request):
    context = {
        "order": Order.objects.all()        
    }
    return render(request, "checkout.html")

# def (request):
