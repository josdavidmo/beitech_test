from rest_framework import serializers

from invoice.models import AvailableProduct, Customer, Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    """
    order serializer.
    """
    total = serializers.SerializerMethodField(help_text='sum(quantity_i*product_price_i)')
    products = serializers.SerializerMethodField(help_text='comma separated list of products and quantities')
    order_details = serializers.JSONField(write_only=True,help_text='[{"product_id": 1,"quantity": 2}]')

    def get_total(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return sum([order_detail.product.price * order_detail.quantity for order_detail in order_details])

    def get_products(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return ','.join(["%s x %s" % (order_detail.quantity, order_detail.product.name) for order_detail in order_details])

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """

        order_details = validated_data.get('order_details')
        if len(order_details) > 5:
            raise serializers.ValidationError("Only 5 products are allowed")
        order = Order()
        order.customer = validated_data.get('customer')
        order.delivery_address = validated_data.get('delivery_address')
        order.date = validated_data.get('date')
        order.save()
        for order_detail in order_details:
            order_detail_obj = OrderDetail(**order_detail)
            order_detail_obj.order = order
            order_detail_obj.save()
            if not AvailableProduct.objects.filter(customer=order.customer, product_id=order_detail_obj.product_id).exists():
                order.delete()
                raise serializers.ValidationError(
                    "Product %s is not valid for the user %s" % (order_detail_obj.product, order.customer))
            order_detail_obj.save()
        return order

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """

        instance.customer = validated_data.get('customer', instance.customer)
        instance.delivery_address = validated_data.get(
            'delivery_address', instance.delivery_address)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = ('customer', 'id', 'delivery_address',
                  'date', 'total', 'products', 'order_details')


class CustomerSerializer(serializers.ModelSerializer):
    """
    customer serializer.
    """
    text = serializers.SerializerMethodField(help_text='customer name')

    def get_text(self, customer):
        return customer.name

    class Meta:
        model = Customer
        fields = ('id', 'text')
