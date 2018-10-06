from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from invoice.renderers import DatatablesRenderer
from django_filters.rest_framework import DjangoFilterBackend
from invoice.models import Order
from invoice.serializers import OrderSerializer


class OrderList(generics.ListCreateAPIView):
    """
    List all order or create a new order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'customer': ['exact'], 'date': ['range']}
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, DatatablesRenderer)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
