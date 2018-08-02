from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=30)

class RegPizza(models.Model):
    type_pizza = models.CharField(max_length=20)
    small_price = models.DecimalField(decimal_places=2, max_digits=4)
    large_price = models.DecimalField(decimal_places=2, max_digits=4)
    # reg_topping = models.ManyToManyField(Topping)

class SicilianPizza(models.Model):
    type_pizza = models.CharField(max_length=20)
    small_price = models.DecimalField(decimal_places=2, max_digits=4)
    large_price = models.DecimalField(decimal_places=2, max_digits=4)
    # sic_topping = models.ManyToManyField(Topping)

class Subs(models.Model):
    type_sub = models.CharField(max_length=30)
    small_price = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    large_price = models.DecimalField(decimal_places=2, max_digits=4)
    sml_cheese_p = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    lrg_cheese_p = models.DecimalField(decimal_places=2, max_digits=4)

class Pasta(models.Model):
    type_pasta = models.CharField(max_length=30)
    pasta_price = models.DecimalField(decimal_places=2, max_digits=4)

class Salads(models.Model):
    type_salad = models.CharField(max_length=30)
    salad_price = models.DecimalField(decimal_places=2, max_digits=4)

class DinnerPlatter(models.Model):
    type_dinner = models.CharField(max_length=30)
    sml_dinner_price = models.DecimalField(decimal_places=2, max_digits=4)
    lrg_dinner_price = models.DecimalField(decimal_places=2, max_digits=4)

class Order(models.Model):
    user = models.CharField(max_length=150)
    pizza = models.CharField(max_length=30)
    yumprice = models.DecimalField(decimal_places=2, max_digits=4)




