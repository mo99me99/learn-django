from django.shortcuts import render
from django.db import connection
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests

# Create your views here.

class HelloView(APIView):

    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('http://127.0.0.1:8001/play/delay/')
        data = response.json()
        return render(request, 'hello.html', {'name':data})

        