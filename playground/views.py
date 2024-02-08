from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):
    # be careful using .only method. if u render product.unit_price for example, you'll have lots of query to the db
    # but using .values method, we don't have this problem. because .values method uses dic
    # queryset = Product.objects.only('id','title')

    # the .defer methods fetchs all info but specified arguments
    queryset = Product.objects.defer('id')

    return render(request, 'hello.html', {'name' : 'Mohammad','products':list(queryset)})
