from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Cart, CartItem, Order, OrderItem
from tags.models import TaggedItem
from .tasks import notify_customers


# Create your views here.
def say_hello(request):
    
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name' : 'Mohammad'})
