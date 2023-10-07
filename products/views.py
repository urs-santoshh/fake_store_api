from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer
from utils.permissions import IsAdminOrReadOnly

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


product_view_set = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail_view_set = ProductViewSet.as_view({'get':'retrieve','patch':'partial_update', 'delete':'destroy'})