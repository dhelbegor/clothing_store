from django.contrib import admin
from apps.stock.models import Product, ProductManagement


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass


@admin.register(ProductManagement)
class ProductManagement(admin.ModelAdmin):
    pass
