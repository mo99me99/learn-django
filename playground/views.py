from django.shortcuts import render
from django.db import connection
import requests

# Create your views here.
def say_hello(request):
    requests.get('http://127.0.0.1:8001/play/delay/')
    return render(request, 'hello.html', {'name':'mohammad'})
