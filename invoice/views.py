from rest_framework import generics

from invoice.models import (AvailableProduct, Customer, Order, OrderDetail,
                            Product)
from invoice.serializers import (AvailableProductSerializer,
                                 CustomerSerializer, OrderDetailSerializer,
                                 OrderSerializer, ProductSerializer)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = ProductSerializer


class AvailableProductList(generics.ListCreateAPIView):
    queryset = AvailableProduct.objects.all()
    serializer_class = AvailableProductSerializer


class AvailableProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AvailableProduct.objects.all()
    serializer_class = AvailableProductSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailList(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class OrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
