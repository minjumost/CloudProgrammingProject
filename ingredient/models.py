from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    ammount = models.IntegerField()
    is_order = models.BooleanField(null=True)
    min_ammount = models.IntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return self.name