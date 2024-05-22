from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Cart, CartItem, Order, OrderItem
from tags.models import TaggedItem
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage


# Create your views here.
def say_hello(request):
    queryset = Product.objects.all()
    try:
        # send_mail('subject', 'message', 'info@mo.com', ['m.m.hosseini1099@gmail.com'])
        # mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('subject', 'message', 'from@mobuy.com', ['m.m.hosseini1099@gmail.com'] )
        # message.attach_file('playground/static/images/DES.png')
        # message.send()
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name' : 'Mohammad'},
        )
        message.attach_file('playground/static/images/DES.png')
        message.send(['m.m.hosseini1099@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name' : 'Mohammad'})
