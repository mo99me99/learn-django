from django.shortcuts import render
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Cart, CartItem, Order, OrderItem
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    
    # use this approach only when you want to do complex queries or performance is not well using ORM
    queryset = Product.objects.raw('select * from store_product') #exact queryset

    with connection.cursor() as cursor: 
        # cursor.execute('') #'queries'
        cursor.callproc('get_customers', [1,2,'a'])
     
    

    return render(request, 'hello.html', {'name' : 'Mohammad','result':list(queryset)})
