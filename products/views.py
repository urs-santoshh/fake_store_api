from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer
from utils.permissions import IsAdminOrReadOnly

class ProductViewSet(ListAPIView):
    queryset = Product.objects.all().order_by('product_id')
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('product_id')
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


product_view_set = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail_view_set = ProductViewSet.as_view({'get':'retrieve','patch':'partial_update', 'delete':'destroy'})