from rest_framework import serializers
from decimal import Decimal

from .models import Cart, CartItem, Customer, Order, OrderItem, Product, Collection, Review


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
        


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']



class CartItemSerializer(serializers.ModelSerializer):

    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    
    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.product.unit_price


    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    cartitem_set = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart:Cart):
        return sum([item.quantity * item.product.unit_price for item in cart.cartitem_set.all()])
    
    class Meta : 
        model = Cart
        fields = ['id','cartitem_set','total_price']



class AddCartItemSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No product with the given ID was found.')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quntity = self.validated_data['quantity']
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quntity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self._validated_data)
        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['quantity']


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    membership = serializers.CharField(read_only=True)
    
    class Meta:
        model = Customer 
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta : 
        model = OrderItem
        fields = ['id', 'product', 'unit_price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):

    orderitem_set = OrderItemSerializer(many=True)
    class Meta: 
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'orderitem_set']