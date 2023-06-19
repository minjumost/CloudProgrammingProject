from django.shortcuts import render, redirect
from .models import Sales
from .utils import best_seller, best_seller_ammount, sales_amount_by_hour
import json


# Create your views here.
def home(request):
    best = json.dumps(best_seller())
    best_ammount = json.dumps(best_seller_ammount())
    time_selling = json.dumps(sales_amount_by_hour())

    return render(
        request,
        'management/home.html',
        {
            'best': best,
            'best_ammount': best_ammount,
            'time_selling': time_selling,
        }
    )

def sale(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        price = request.POST.get('price')

        Sales.objects.create(product=product, price=price)

        return redirect('/menu')

    return render(request, '/menu')


def staff(request):
    return render(
        request,
        'management/home.html',
    )
