from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField()
    min_stock = models.IntegerField()
    order_quantity = models.IntegerField()
    exp_date = models.DateField()
    is_expired = models.BooleanField(null=True)
    need_order = models.BooleanField(null=True)
    def __str__(self):
        return self.name