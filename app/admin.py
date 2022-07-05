from unicodedata import category
from django.contrib import admin
from .models import * 



class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "category")
    
admin.site.register(Product, ProductAdmin)


class ProductColorSizeAdmin(admin.ModelAdmin):
    list_display = ("productColor", "memory", "price")

admin.site.register(ProductColorSize, ProductColorSizeAdmin)


class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("product", "color")

admin.site.register(ProductColor, ProductColorAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", 'quantity')

admin.site.register(Cart, CartAdmin)

admin.site.register(Favourite)

class StorageAdmin(admin.ModelAdmin):
    list_display = ("productColorSize", "quantity", 'storage_type', 'date')

admin.site.register(Storage, StorageAdmin)



admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)

admin.site.register(Memory)
admin.site.register(ProductGallery)

admin.site.register(Order)
admin.site.register(View)

admin.site.register(OrderProduct)