from django.contrib import admin
from .models import Beverage, Ingredient, Recipt
# Register your models here.
admin.site.register(Beverage)
admin.site.register(Ingredient)
admin.site.register(Recipt)