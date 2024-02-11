from typing import Any
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib import admin, messages
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models



class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'
    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('<10', 'Low')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        

# customize admin model of a class 
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ['title', 'slug']
    # exclude  = ['title', 'slug']
    # readonly_fields = ['slug']
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug' :['title']
    }

    actions = ['clear_inventory']
    list_display = ['title', 'unit_price','inventory','inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 20
    list_filter = ['collection','last_update', InventoryFilter]
    search_fields = ['title__istartswith']

    # like select related in queries
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    def collection_title(self, product):
        return product.collection.title
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            message=messages.SUCCESS
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership','orders_count']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    list_filter = ['membership']
    list_per_page = 20

    @admin.display(ordering='orders_count')
    def orders_count(self, customer): 
        url = (
            reverse('admin:store_order_changelist') 
            + '?'
            + urlencode({'customer__id':str(customer.id)}))
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)
         

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(orders_count=Count('order'))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['pk','customer','payment_status','placed_at']
    ordering = ['placed_at']
    list_filter = ['customer__id']
    list_per_page = 20

    


# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['featured_product']
    list_display = ['title', 'products_count']
    search_fields = ['title__istartswith']

    @admin.display(ordering='products_count')
    def products_count(self, collection): 

        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({'collection__id':str(collection.id)}))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
         

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(products_count=Count('product'))

# admin.site.register(models.Product)
# admin.site.register(models.Product, ProductAdmin)