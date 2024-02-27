from rest_framework import serializers
from decimal import Decimal

from .models import Cart, Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Collection
        fields = ['id', 'title', 'products_count']
        
    products_count = serializers.IntegerField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','slug','inventory', 'unit_price','description','collection','collection_title','price_with_tax']
        # fields = '__all__' #bad practice

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection_title = serializers.SerializerMethodField(method_name='get_collection_title')

    def get_collection_title(self, product:Product):
        return product.collection.title

    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)
    
    # create and update methods are available and could be override


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
        


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    class Meta : 
        model = Cart
        fields = ['id']


