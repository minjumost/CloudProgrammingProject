from django.utils import timezone
from .models import Ingredient

def update_expired():
    current_date = timezone.now().date()
    ingredients = Ingredient.objects.all()

    for ingredient in ingredients:
        if ingredient.exp_date < current_date:
            ingredient.is_expired = True
        else:
            ingredient.is_expired = False
        ingredient.save()