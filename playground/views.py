from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Cart, CartItem, Order, OrderItem
from tags.models import TaggedItem
from django.core.mail import send_mail, mail_admins, BadHeaderError


# Create your views here.
def say_hello(request):
    queryset = Product.objects.all()
    try:
        # send_mail('subject', 'message', 'info@mo.com', ['m.m.hosseini1099@gmail.com'])
        mail_admins('subject', 'message', html_message='message')
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name' : 'Mohammad'})
