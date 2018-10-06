from rest_framework import serializers

from invoice.models import (LANGUAGE_CHOICES, STYLE_CHOICES, AvailableProduct,
                            Customer, Order, OrderDetail, Product)


class ProductSerializer(serializers.ModelSerializer):
    """
    product serializer.
    """

    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    """
    customer serializer.
    """

    class Meta:
        model = Customer
        fields = '__all__'


class AvailableProductSerializer(serializers.ModelSerializer):
    """
    avaiable product serializer.
    """

    class Meta:
        model = AvailableProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
    order serializer.
    """

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    order detail serializer.
    """

    class Meta:
        model = OrderDetail
        fields = '__all__'
