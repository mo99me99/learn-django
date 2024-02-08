from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):
    # Products: inventory = price
    queryset = Product.objects.filter(inventory= F('collection__id'))
    return render(request, 'hello.html', {'name' : 'Mohammad','products':list(queryset)})
