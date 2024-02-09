from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    TaggedItem.objects.get_tags_for(Product,1)
    

    return render(request, 'hello.html', {'name' : 'Mohammad','tags':list(queryset)})
