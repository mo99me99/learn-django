from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline




# Register your models here.
class TagInline(GenericTabularInline):
    model = TaggedItem
    min_num =0
    max_num = 10
    extra = 0
    autocomplete_fields = ['tag']



class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]
    
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
