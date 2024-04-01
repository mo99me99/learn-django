from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import User



# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'first_name', 'last_name'),
            },
        ),
    )


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
