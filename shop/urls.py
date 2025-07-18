
from shop.views import detail, home, products
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('detail/<int:pk>/', detail, name='detail'),
]
