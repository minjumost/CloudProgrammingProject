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

def home(request):
    return render(
        request,
        'ingredient/home.html',
    )