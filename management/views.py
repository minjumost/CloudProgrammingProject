from django.shortcuts import render, redirect
from beverage.models import Beverage, Recipt
from ingredient.models import Ingredient
from .models import Sales
from .utils import best_seller, best_seller_ammount, sales_amount_by_hour, daily_income, last_week_income
import json
from ingredient.utils import expired, need_to_order


# Create your views here.
def home(request):
    best = json.dumps(best_seller())
    best_ammount = json.dumps(best_seller_ammount())
    time_selling = json.dumps(sales_amount_by_hour())
    today_income = daily_income()
    last_income = last_week_income()
    expired_ingredients = expired()
    empty_ingredients = need_to_order()


    return render(
        request,
        'management/home.html',
        {
            'best': best,
            'best_ammount': best_ammount,
            'time_selling': time_selling,
            'today_income': today_income,
            'last_income' : today_income-last_income,
            'expired_ingredients': expired_ingredients,
            'empty_ingredients' : empty_ingredients,
        }
    )

def sale(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        price = request.POST.get('price')

        #판매정보 등록
        Sales.objects.create(product=product, price=price)

        #판매된 음료의 재고량 업데이트
        recipts = Recipt.objects.filter(beverage__name=product)
        for recipt in recipts:
            quantity = recipt.quantity
            recipt.ingredients.ammount -= quantity
            recipt.ingredients.save()

        return redirect('/menu')

    return render(request, '/menu')


def staff(request):
    return render(
        request,
        'management/home.html',
    )
