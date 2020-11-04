from rest_framework import serializers

from .models import Product, ProductManagement


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'image_url', 'quantity', 'category', 'size', 'price', 'sold_off']
        read_only_fields = ['id', 'sold_off']


class ProductManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManagement
        fields = ['id', 'product', 'sell_per_day', 'total_sell', 'month']
        read_only_fields = ['id']


class ProductImportSerializer(serializers.Serializer):
    file_upload = serializers.FileField()
