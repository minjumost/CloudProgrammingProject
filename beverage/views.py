from django.shortcuts import render
from .models import Beverage, Recipt

# Create your views here.
def menu(request):
    beverages = Beverage.objects.all()
    return render(
        request,
        'beverage/menu.html',
        {
            'beverages': beverages,
        }
    )
def recipt(request, beverage_name):
    recipt = Recipt.objects.filter(beverage__name=beverage_name)

    return render(
        request,
        'beverage/recipt.html',
        {
            'recipt': recipt,
        }
    )
