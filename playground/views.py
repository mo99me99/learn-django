from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    
    queryset = Product.objects.all()
    list(queryset)
    list(queryset)
    queryset[0]
    

    return render(request, 'hello.html', {'name' : 'Mohammad','tags':list(queryset)})
