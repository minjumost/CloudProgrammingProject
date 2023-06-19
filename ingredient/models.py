from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    ammount = models.IntegerField()
    min_ammount = models.IntegerField()
    exp_date = models.DateField()
    is_expired = models.BooleanField(null=True)
    need_order = models.BooleanField(null=True)
    def __str__(self):
        return self.name