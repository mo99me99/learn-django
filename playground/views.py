from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product,Customer,Collection,Order,OrderItem



# Create your views here.
def say_hello(request):
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    # • Customers with their last order ID 
    # • Collections and count of their products  
    # • Customers with more than 5 orders  
    # • Customers and the total amount they’ve spent  
    # • Top 5 best-selling products and their total sales  
    # queryset = Customer.objects.annotate(last_order=Max('order__id'))
    # queryset = Collection.objects.annotate(prods_count=Count('product'))
    # queryset = Customer.objects.annotate(order_count=Count('order')).filter(order_count__gt=5)
    # queryset = Customer.objects.annotate(total_spent=Sum( F('order__orderitem__unit_price') * F('order__orderitem__quantity') )).order_by('-total_spent')

    queryset = Product.objects.annotate(
        total_sale=Sum( F('orderitem__unit_price') * F('orderitem__quantity'))) \
        .annotate(quntity_soled=Sum(F('orderitem__quantity'))).order_by('-total_sale')[:5]

    return render(request, 'hello.html', {'name' : 'Mohammad','result':list(queryset)})
