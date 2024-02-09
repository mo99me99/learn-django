from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    
    collection = Collection(pk=11)
    collection.delete()

    # collection.objects.filter(id__gt=5).delete()
    
    


    return render(request, 'hello.html', {'name' : 'Mohammad','tags':list()})
