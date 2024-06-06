from django.shortcuts import render
from django.db import connection
from django.core.cache import cache
import requests

# Create your views here.
def say_hello(request):
    key = 'httpbin_result'
    if cache.get(key) is None:
        response = requests.get('http://127.0.0.1:8001/play/delay/')
        data = response.json()
        cache.set(key, data)
    return render(request, 'hello.html', {'name':cache.get(key)})
