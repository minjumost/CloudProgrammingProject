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

def expired():
    expired_ingredients = Ingredient.objects.filter(is_expired=True)
    total_expired = 0

    for i in expired_ingredients:
        total_expired += 1

    return total_expired

def need_to_order():
    empty_ingredients = Ingredient.objects.filter(need_order=True)
    total_empty = 0

    for i in empty_ingredients:
        total_empty +=1

    return total_empty