from django_filters import rest_framework as filters

from orders.models import Order

class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['status']
