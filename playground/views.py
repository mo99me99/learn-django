from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):

    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20)) #or
    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20)) #and : but no need ot use '&'. you can use filters one after each
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)) # x and not(y)
    
    return render(request, 'hello.html', {'name' : 'Mohammad','products':list(queryset)})
