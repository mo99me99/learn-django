from django.contrib import admin
from . import models

# customize admin model of a class 
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory','inventory_status']
    list_editable = ['unit_price']
    list_per_page = 20

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20

# Register your models here.
admin.site.register(models.Collection)

# admin.site.register(models.Product)
# admin.site.register(models.Product, ProductAdmin)