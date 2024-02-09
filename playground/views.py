from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    
    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Game'
    # collection.featured_product = None
    # collection.save()

    Collection.objects.filter(pk=11).update(featured_product=None)

    


    return render(request, 'hello.html', {'name' : 'Mohammad','tags':list()})
