from django.contrib import admin

# Register your models here.

from .models import Topping, RegPizza, SicilianPizza, Subs, Pasta, Salads, DinnerPlatter


admin.site.register(Topping)
admin.site.register(RegPizza)
admin.site.register(SicilianPizza)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatter)