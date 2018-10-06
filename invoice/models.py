from django.db import models


class Product(models.Model):
    """
    table for product.
    """

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    product_description = models.TextField()


class Customer(models.Model):
    """
    table for customer.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()


class AvailableProduct(models.Model):
    """
    table for available product.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    """
    table for order.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100)
    date = models.TimeField(auto_now=True)


class OrderDetail(models.Model):
    """
    table for order detail.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
