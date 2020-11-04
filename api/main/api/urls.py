from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('stock/', include('apps.stock.urls', namespace='stock')),
]
