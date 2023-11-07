from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from products.models import Product

User = get_user_model()


class Cart(models.Model):

    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.user.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Total cost of all the items in an cart
        """
        return round(sum([cart_item.cost for cart_item in self.cart_items.all()]), 2)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="cart_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product_cart", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.cart.user.get_full_name()

    @cached_property
    def cost(self):
        """
        Total cost of the cart item
        """
        return round(self.quantity * self.product.price, 2)
