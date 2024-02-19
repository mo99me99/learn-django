from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


# Create your views here.


class ProductList(ListCreateAPIView):

    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request', self.request}
    

class ProductDetail(APIView):

    def get(self, request, pk):
        product:Product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        product:Product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        product:Product = get_object_or_404(Product, pk=pk)
        if product.orderitem_set.count() > 0 :
            return Response({'error':'product can not be deleted because it is associated with an order item'}
                            ,status=status.HTTP_405_METHOD_NOT_ALLOWED
                    )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionSerializer
    


@api_view(['GET','DELETE', 'PUT'])
def collection_detail(request,pk):
    collection:Collection = get_object_or_404(Collection.objects.annotate(products_count=Count('product')), pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection, context={'request':request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)     
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    elif request.method == 'DELETE' : 
        if collection.product_set.count() > 0 :
            return Response(
                {'error':'collection can not be deleted because it is associated with a(some) product(s)'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  