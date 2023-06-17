from django.shortcuts import render
from .models import Ingredient
# Create your views here.
def ingredient(request):
    ingredients = Ingredient.objects.all()
    return render(
        request,
        'ingredient/ingredient.html',
        {
            'ingredients': ingredients,
        }
    )

def stock(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    return render(
        request,
        'ingredient/stock.html',
        {
            'ingredient': ingredient,
        }
    )