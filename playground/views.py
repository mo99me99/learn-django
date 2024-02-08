from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum 
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):
    
    # result = Product.objects.aggregate(Count('id'))
    # result = Product.objects.aggregate(count=Count('id'))
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    # result = Product.objects.filter(collection__id=5).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # • How many orders do we have?  
    # result = Order.objects.aggregate(order_count=Count('id'))
    # • How many units of product 1 have we sold?  
    # result = OrderItem.objects.filter(order__payment_status='C', product_id=1).aggregate(units_sold=Sum('quantity'))
    # • How many orders has customer 1 placed?  
    # result = Order.objects.filter(customer_id=1).aggregate(count=Count('id'))
    # • What is the min, max and average price of the products in collection 3?  
    result = Product.objects.filter(collection_id=3).aggregate(min=Min('unit_price'), max=Max('unit_price'),avg=Avg('unit_price'))


    return render(request, 'hello.html', {'name' : 'Mohammad','result':result})
