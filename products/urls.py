from django.urls import path

from .views import product_view_set, product_detail_view_set

urlpatterns = [
    path('', product_view_set, name="product_viewsets"),
    path('<str:pk>/', product_detail_view_set, name="product_detail_viewsets"),
]