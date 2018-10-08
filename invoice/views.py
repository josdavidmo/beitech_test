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

    List the orders is filter by the customer and created date, one example of
    request is:
        - http://localhost:8000/invoice/order/?format=datatables&customer=1, if you want filter only by customer
        - http://localhost:8000/invoice/order/?format=datatables&customer=1&date=2018-10-01, if you want filter by customer and specific date
        - http://localhost:8000/invoice/order/?format=datatables&customer=1&date__range=2018-10-01,2018-10-05, if you want filter by customer and specific range date

    The previous request returns data as the next example
        {"data":[
            {"customer":1,"id":1,
            "delivery_address":"Calle 26c #13-97",
            "date":"2018-10-01",
            "total":42271,
            "products":"Arroz,Azúcar,Consomate"},
            {"customer":1,"id":2,
            "delivery_address":"Calle 26c #13-97",
            "date":"2018-10-01",
            "total":31396,
            "products":"Sopa,Consomate"}]}
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'customer': ['exact'], 'date': ['range', 'exact']}
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, DatatablesRenderer)


class CustomerList(generics.ListAPIView):
    """
    List all customer.

    One example of the possible output is the next:
     [{"id":1,"text":"Manny Bharma"},
      {"id":2,"text":"Alan Briggs"},
      {"id":3,"text":"Mike Simm"}]
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend,)
