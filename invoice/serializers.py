from rest_framework import serializers

from invoice.models import Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    """
    order serializer.
    """
    total = serializers.SerializerMethodField('cal_total')
    products = serializers.SerializerMethodField('list_products')

    def cal_total(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return sum([order_detail.product.price * order_detail.quantity for order_detail in order_details])

    def list_products(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return ','.join([order_detail.product.name for order_detail in order_details])

    class Meta:
        model = Order
        fields = ('customer', 'id', 'delivery_address',
                  'date', 'total', 'products')
