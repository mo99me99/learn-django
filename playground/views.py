from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.
def say_hello(request):
    try:
        product = Product.objects.get(pk=1)
    except ObjectDoesNotExist:
        pass
    
    return render(request, 'hello.html', {'name' : 'Mohammad'})
