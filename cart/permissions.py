from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission

from cart.models import Cart


class IsCartItemByUserOrAdmin(BasePermission):
    """
    Check if cart item is owned by appropriate user or admin
    """

    def has_permission(self, request, view):
        cart_id = view.kwargs.get("cart_id")
        cart = get_object_or_404(Cart, id=cart_id)
        return cart.user == request.user or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.cart.user == request.user or request.user.is_staff


class IsCartByUserOrAdmin(BasePermission):
    """
    Check if cart is owned by appropriate user or admin
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated is True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


