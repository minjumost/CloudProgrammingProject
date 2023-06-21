from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from beverage.models import Recipt
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
        'management/index.html',
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

        recipts = Recipt.objects.filter(beverage__name=product)


        #판매된 음료의 재고량 업데이트
        for recipt in recipts:
            quantity = recipt.quantity
            recipt.ingredients.stock -= quantity

            #소비기한이 지난 재료가 없는지 검사
            if (recipt.ingredients.is_expired):
                message = "소비기한을 확인해주세요!"
                return render(
                    request,
                    'management/notice.html',
                    {
                        'message': message
                    }
                )

            #수량이 부족한 재료가 없는지 검사
            if(recipt.ingredients.stock < 0):
                message = "재고가 부족합니다!"
                return render(
                    request,
                    'management/notice.html',
                    {
                        'message': message
                    }
                )

            recipt.ingredients.save()

        # 판매정보 등록
        Sales.objects.create(product=product, price=price)
        messages.success(request, product+' 판매 완료 (+'+ price+'원)' )

        return redirect('/menu')

    return render(request, '/menu')


class Login(LoginView):
   template_name = 'management/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'management/notice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "로그아웃되었습니다."
        return context

def need_login(request):
    message = "로그인 해주세요!"
    return render(
        request,
        'management/notice.html',
        {
            'message': message
        }
    )

def permission_denied(request):
    message = "권한이 없습니다!"
    return render(
        request,
        'management/notice.html',
        {
            'message': message
        }
    )