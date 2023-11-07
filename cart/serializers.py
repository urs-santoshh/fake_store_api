from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing cart items
    """

    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = (
            "id",
            "cart",
            "product",
            "quantity",
            "price",
            "cost",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("cart",)

    def validate(self, validated_data):
        cart_quantity = validated_data["quantity"]
        product_quantity = validated_data["product"].quantity

        cart_id = self.context["view"].kwargs.get("cart_id")
        product = validated_data["product"]
        current_item = CartItem.objects.filter(
            cart__id=cart_id, product=product)

        if cart_quantity > product_quantity:
            error = {"quantity": _("Quantity is more than the stock.")}
            raise serializers.ValidationError(error)

        if not self.instance and current_item.count() > 0:
            error = {"product": _("Product already exists in your cart.")}
            raise serializers.ValidationError(error)

        if self.context["request"].user == product.seller:
            error = _("Adding your own product to your cart is not allowed")
            raise PermissionDenied(error)

        return validated_data

    def get_price(self, obj):
        return obj.product.price

    def get_cost(self, obj):
        return obj.cost


class CartReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading carts
    """

    user = serializers.CharField(source="user.get_full_name", read_only=True)
    cart_items = CartItemSerializer(read_only=True, many=True)
    total_cost = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "cart_items",
            "total_cost",
            "created_at",
            "updated_at",
        )

    def get_total_cost(self, obj):
        return obj.total_cost


class CartWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for creating cart and cart items

    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "cart_items",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        cart_data = validated_data.pop("cart_items")
        cart = Cart.objects.create(**validated_data)

        for data in cart_data:
            CartItem.objects.create(cart=cart, **data)

        return cart

    def update(self, instance, validated_data):
        cart_data = validated_data.pop("cart_items", None)
        cart = list((instance.cart_items).all())

        if cart_data:
            for cart_data in cart_data:
                cart = cart.pop(0)
                cart.product = cart_data.get("product", cart.product)
                cart.quantity = cart_data.get("quantity", cart.quantity)
                cart.save()

        return instance
