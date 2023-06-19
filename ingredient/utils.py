from django.utils import timezone
from .models import Ingredient

def update_expired():
    today = timezone.now().date()
    ingredients = Ingredient.objects.all()

    for i in ingredients:
        if i.exp_date < today:
            i.is_expired = True
        else:
            i.is_expired = False
        i.save()

def update_need_order_status():
    ingredients = Ingredient.objects.all()

    for i in ingredients:
        if i.ammount < i.min_ammount:
            i.need_order = True
        else:
            i.need_order = False
        i.save()