from django.urls import path

from . import views

app_name = 'stock'
urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name="products-list-create"),
    path('products/<int:pk>/', views.ProductRetrieve.as_view(), name='products-retrieve'),
    path('products/management/', views.ProductManagementListCreate.as_view(), name="products-management-list-create"),
    path('products/<int:pk>/management/', views.ProductManagementRetrieve.as_view(),
         name='products-management-retrieve'),
    path('products/import/', views.ProductImport.as_view(), name="products-import"),
]
