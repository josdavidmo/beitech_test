from rest_framework import serializers

from invoice.models import (LANGUAGE_CHOICES, STYLE_CHOICES, AvailableProduct,
                            Customer, Order, OrderDetail, Product)


class ProductSerializer(serializers.Serializer):
    """
    product serializer.
    """

    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.Serializer):
    """
    customer serializer.
    """

    class Meta:
        model = Customer
        fields = '__all__'


class AvailableProductSerializer(serializers.Serializer):
    """
    avaiable product serializer.
    """

    class Meta:
        model = AvailableProduct
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    """
    order serializer.
    """

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.Serializer):
    """
    order detail serializer.
    """

    class Meta:
        model = OrderDetail
        fields = '__all__'
