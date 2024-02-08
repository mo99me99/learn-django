from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Customer,Collection,Order,OrderItem


# Create your views here.
def say_hello(request):

    # queryset = Product.objects.values('id','title','collection__title')
    # queryset = Product.objects.values_list('id','title','collection__title')
    ordered_prods_ids = OrderItem.objects.values('product_id').distinct() #distinct removes dublicates
    queryset = Product.objects.filter(id__in=ordered_prods_ids).order_by('title')


    return render(request, 'hello.html', {'name' : 'Mohammad','products':list(queryset)})
