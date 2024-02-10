from django.contrib import admin
from . import models

# customize admin model of a class 
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price','inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 20

    # like select related in queries
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    def collection_title(self, product):
        return product.collection.title



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk','customer','payment_status','placed_at']
    ordering = ['placed_at']
    list_per_page = 20

    


# Register your models here.
admin.site.register(models.Collection)

# admin.site.register(models.Product)
# admin.site.register(models.Product, ProductAdmin)