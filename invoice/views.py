from rest_framework import generics

from invoice.models import (AvailableProduct, Customer, Order, OrderDetail,
                            Product)
from invoice.serializers import (AvailableProductSerializer,
                                 CustomerSerializer, OrderDetailSerializer,
                                 OrderSerializer, ProductSerializer)


class ProductLC(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerLC(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = ProductSerializer


class AvailableProductLC(generics.ListCreateAPIView):
    queryset = AvailableProduct.objects.all()
    serializer_class = AvailableProductSerializer


class AvailableProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AvailableProduct.objects.all()
    serializer_class = AvailableProductSerializer


class OrderLC(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailLC(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class OrderDetailRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
