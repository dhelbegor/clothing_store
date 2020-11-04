import logging

from rest_framework import status, generics, permissions
from django.shortcuts import get_object_or_404
from apps.stock.models import Product, ProductManagement
from apps.stock.serializers import ProductSerializer, ProductImportSerializer, ProductManagementSerializer
from main.import_lib.factory import ImportFactory
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductManagementListCreate(generics.ListCreateAPIView):
    queryset = ProductManagement.objects.all()
    serializer_class = ProductManagementSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductManagementRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductManagementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        product_id = self.kwargs.get('pk', None)
        return get_object_or_404(ProductManagement, product_id=product_id)

    def get_queryset(self):
        product_id = self.kwargs.get('pk', None)
        return ProductManagement.objects.filter(product_id=product_id)


class ProductImport(generics.GenericAPIView):
    serializer_class = ProductImportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_file = serializer.validated_data.get('file_upload')
            products = ImportFactory.get_csv(validated_file.temporary_file_path())

            for product in products:
                management = product.copy()
                product.pop('sell_per_day')
                product.pop('total_sell')
                product.pop('month')
                created, _ = Product.objects.update_or_create(sku=product['sku'], defaults=product)
                logger.info(f'created/updated product_id {created.id} from csv import.')

                product_management = ProductManagement.objects.create(
                    product_id=created.id,
                    sell_per_day=management['sell_per_day'],
                    total_sell=management['total_sell'],
                    month=management['month']
                )
                logger.info(f'created producut_management_id {product_management.id} from csv import.')

            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors)
