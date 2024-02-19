from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Collection, OrderItem, Product
from .serializers import CollectionSerializer, ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request', self.request}
    
    def destroy(self, request, *args, **kwargs):
        product:Product = get_object_or_404(Product, pk=kwargs['pk'])
        if product.orderitem_set.count() > 0 :
            return Response({'error':'product can not be deleted because it is associated with an order item'}
                            ,status=status.HTTP_405_METHOD_NOT_ALLOWED
                    )
        return super().destroy(request, *args, **kwargs)
    



class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionSerializer


    def destroy(self, request, *args, **kwargs):
        if Collection.objects.filter(product_id=kwargs['pk']).count() > 0 : 
            return Response(
                {'error':'collection can not be deleted because it is associated with a(some) product(s)'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )

        return super().destroy(request, *args, **kwargs)