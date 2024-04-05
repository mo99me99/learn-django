from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser, DjangoModelPermissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin, ListModelMixin

from .permissions import IsAdminOrReadOnly
from .pagination import DefaultPagination
from .filters import ProductFilter
from .models import CartItem, Collection, Customer, OrderItem, Product, Review, Cart
from .serializers import AddCartItemSerializer, CartItemSerializer, CartSerializer, CollectionSerializer, CustomerSerializer, ProductSerializer, ReviewSerializer, UpdateCartItemSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    permission_classes = [IsAdminOrReadOnly]



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

    permission_classes = [IsAdminOrReadOnly]


    def destroy(self, request, *args, **kwargs):
        if Collection.objects.filter(product_id=kwargs['pk']).count() > 0 : 
            return Response(
                {'error':'collection can not be deleted because it is associated with a(some) product(s)'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )

        return super().destroy(request, *args, **kwargs)
    


class ReviewViewSet(ModelViewSet):

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
    serializer_class = ReviewSerializer
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
    


class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.prefetch_related('cartitem_set__product').all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    # method names should be in lowercase
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_class(self):
        if self.request.method == 'POST' : 
            return AddCartItemSerializer
        if self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get', 'put'], permission_classes=[IsAuthenticated] )
    def me(self, request):

        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)

        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        
        if request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
