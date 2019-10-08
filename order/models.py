from typing import List

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import TextInput, ModelForm

from product.models import Product


class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product

    @property
    def amount(self):
        return (self.quantity * self.product.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity']
        widgets = {
            'quantity': TextInput(attrs={'class': 'input', 'type': 'number', 'value': '1', 'placeholder': 'adet'}),

        }


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshipping', 'Onshipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    total = models.FloatField()
    note = models.TextField(null=True, default="")
    status = models.CharField(choices=STATUS, default='New', max_length=15)
    creatat = models.DateTimeField(auto_now_add=True)
    updateat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'address', 'city', 'phone']
        widgets = {

            'name': TextInput(attrs={'class': 'input', 'type': 'text', }),
            'surname': TextInput(attrs={'class': 'input', 'type': 'text', }),
            'address': TextInput(attrs={'class': 'input', 'type': 'text', }),
            'city': TextInput(attrs={'class': 'input', 'type': 'text', }),
            'phone': TextInput(attrs={'class': 'input', 'type': 'text', }),


        }


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    creatat = models.DateTimeField(auto_now_add=True)
    updateat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
