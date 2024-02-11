from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


# Create your views here.


@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response('OK')


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product, context={'request':request})
    return Response(serializer.data)


@api_view()
def collection_list(request):
    queryset = Collection.objects.all()
    serializer = CollectionSerializer(queryset, many=True, context={'request':request})
    return Response(serializer.data)


@api_view()
def collection_detail(request,pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection, context={'request':request})
    return Response(serializer.data)