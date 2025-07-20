
from shop.views import IndexView, Products, Detail, Order_View
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('products/', Products.as_view(), name='products'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('order/<int:pk>', Order_View.as_view(), name='order')
]
