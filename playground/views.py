from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):
    # Products: inventory = price
    # queryset = Product.objects.order_by('title')
    # queryset = Product.objects.order_by('-title')
    # queryset = Product.objects.order_by('unit_price','title')
    # queryset = Product.objects.order_by('unit_price','title').reverse()
    queryset = Product.objects.filter(collection__pk=3).order_by('unit_price')
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')

    return render(request, 'hello.html', {'name' : 'Mohammad','products':list(queryset)})
