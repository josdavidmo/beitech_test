from rest_framework import serializers

from invoice.models import AvailableProduct, Customer, Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    """
    order serializer.
    """
    total = serializers.SerializerMethodField('cal_total')
    products = serializers.SerializerMethodField('list_products')
    order_details = serializers.JSONField(write_only=True)

    def cal_total(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return sum([order_detail.product.price * order_detail.quantity for order_detail in order_details])

    def list_products(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return ','.join(["%s x %s" % (order_detail.quantity, order_detail.product.name) for order_detail in order_details])

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        order_details param must be an json list like this
        {
          "customer": 1,
          "delivery_address": "Diagonal 86a # 101 - 40",
          "date": "2018-10-06",
          "order_details": [
            {
              "product_id": 1,
              "quantity": 2
            },
            {
              "product_id": 2,
              "quantity": 1
            },
            {
              "product_id": 3,
              "quantity": 41
            },
            {
              "product_id": 4,
              "quantity": 54
            }
          ]
        }
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
    text = serializers.SerializerMethodField('get_string')

    def get_string(self, customer):
        return customer.name

    class Meta:
        model = Customer
        fields = ('id', 'text')
