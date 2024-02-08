from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum 
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):
    # usign db fucntions
    # queryset = Customer.objects.annotate(
    #     # CONCAT
    #     full_name = Func(F('first_name'),Value(' '), F('last_name'), function='CONCAT')
    # )

    queryset = Customer.objects.annotate(
        # Concat
        full_name = Concat('first_name',Value(' '), 'last_name')
    )

    # you can search for django db functions 

    return render(request, 'hello.html', {'name' : 'Mohammad','result':list(queryset)})
