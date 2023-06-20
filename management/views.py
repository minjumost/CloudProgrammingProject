from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from beverage.models import  Recipt
from .models import Sales
from .utils import best_seller, best_seller_ammount, sales_amount_by_hour, daily_income, last_week_income, \
    manager_required
import json
from ingredient.utils import expired, need_to_order
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

def home(request):
    return render(
        request,
        'management/home.html',
    )
@login_required
@manager_required
def dashboard(request):
    best = json.dumps(best_seller())
    best_ammount = json.dumps(best_seller_ammount())
    time_selling = json.dumps(sales_amount_by_hour())
    today_income = daily_income()
    last_income = last_week_income()
    expired_ingredients = expired()
    empty_ingredients = need_to_order()


    return render(
        request,
        'management/dashboard.html',
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

@login_required
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


class Login(LoginView):
   template_name = 'management/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'management/login.html'

def need_login(request):
    return render(
        request,
        'management/need_login.html',
    )

def permission_denied(request):
    return render(
        request,
        'management/permission_denied.html',
    )