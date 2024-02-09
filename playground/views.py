from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Cart, CartItem
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
    
    # • Create a shopping cart with an item 
    # cart = Cart()
    # cart.save()
    # cart_item = CartItem()
    # cart_item.cart = cart
    # cart_item.product_id = 11
    # cart_item.quantity = 10
    # cart_item.save()

    # • Update the quantity of an item in a shopping cart
    # item = CartItem.objects.get(pk=1)
    # item.quantity=2
    # item.save()
    
    # • Remove a shopping cart with its items  
    # cart = Cart.objects.get(pk=1)
    # cart.delete()




    return render(request, 'hello.html', {'name' : 'Mohammad','tags':list()})
