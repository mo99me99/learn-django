from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    
    # first approach 
    # collection = Collection(title='Video Game')
    collection = Collection()
    collection.title = 'Video Game'
    collection.featured_product = Product(pk=1)
    # collection.featured_product_id = 1 
    collection.save()

    # second approach
    # collection = Collection.objects.create(title='Video Game', featured_product_id=1)


    return render(request, 'hello.html', {'name' : 'Mohammad','tags':list()})
