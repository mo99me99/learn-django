from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum 
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):

    queryset = Customer.objects.annotate(
        order_count = Count('order')
    )

    # you can search for django db functions 

    return render(request, 'hello.html', {'name' : 'Mohammad','result':list(queryset)})
