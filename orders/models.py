from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Topping(models.Model):
#     name = models.CharField(max_length=30)

# class Pizza(models.Model):
#     name = models.CharField(max_length=50)
#     toppings = models.ManyToManyField(Topping, through='PizzaToppingsThroughModel')

#     def __str__(self):
#         return "%s (%s)" % (
#             self.name,
#             ", ".join(topping.name for topping in self.toppings.all()),
#         )

# class PizzaToppingsThroughModel(OrderedModel):
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#     topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
#     order_with_respect_to = 'pizza'

#     class Meta:
#         ordering = ('pizza', 'order')

# class Login(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

# class Pizza

