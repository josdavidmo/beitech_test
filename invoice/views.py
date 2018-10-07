from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response

from invoice.models import Customer, Order
from invoice.renderers import DatatablesRenderer
from invoice.serializers import CustomerSerializer, OrderSerializer


class OrderList(generics.ListCreateAPIView):
    """
    List all order or create a new order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'customer': ['exact'], 'date': ['range','exact']}
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, DatatablesRenderer)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CustomerList(generics.ListCreateAPIView):
    """
    List all customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend,)
