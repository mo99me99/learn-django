from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


# Create your views here.
class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request', self.request}

    def delete(self, request, pk):
        product:Product = get_object_or_404(Product, pk=pk)
        if product.orderitem_set.count() > 0 :
            return Response({'error':'product can not be deleted because it is associated with an order item'}
                            ,status=status.HTTP_405_METHOD_NOT_ALLOWED
                    )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CollectionViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionSerializer
    

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.product_set.count() > 0 :
            return Response(
                {'error':'collection can not be deleted because it is associated with a(some) product(s)'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  