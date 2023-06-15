from django.db import models
from ingredient.models import Ingredient
# Create your models here.


class Beverage(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, through='Recipt')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/menu/{self.name}'

class Recipt(models.Model):
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.beverage.name+' 레시피'