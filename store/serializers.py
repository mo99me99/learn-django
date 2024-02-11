from rest_framework import serializers
from decimal import Decimal

from store.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)




class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(source='unit_price',max_digits=9,decimal_places=3)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all() 
    # )
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )
    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)
    
