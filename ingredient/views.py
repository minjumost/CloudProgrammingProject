from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from management.utils import ManagerRequiredMixin, manager_required
from .models import Ingredient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .utils import update_expired, update_need_order_status
# Create your views here.


class ViewIngredients(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'ingredient/list_ingredient.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        update_expired()
        update_need_order_status()
        return queryset
class CreateIngredient(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name', 'stock', 'min_stock', 'order_quantity', 'exp_date', ]
    labels = {
        'name': '이름',
        'stock': '재고량(g, mL)',
        'min_stock': '최소 유지 수량(g, mL)',
        'exp_date': '소비 기한(yyyy-mm-dd)',
        'order_quantity': '주문량',
    }
    template_name = 'ingredient/create_ingredient.html'
    success_url = '/stock/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, label in self.labels.items():
            form.fields[field_name].label = label
        return form

class UpdateIngredient(LoginRequiredMixin, ManagerRequiredMixin, UpdateView):
    model = Ingredient
    fields = ['name', 'stock', 'min_stock', 'order_quantity', 'exp_date', ]
    labels = {
        'name': '이름',
        'stock': '재고량(g, mL)',
        'min_stock': '최소 유지 수량(g, mL)',
        'exp_date': '소비 기한(yyyy-mm-dd)',
        'order_quantity': '주문량',
    }
    success_url = '/stock/'
    template_name = 'ingredient/update_ingredient.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, label in self.labels.items():
            form.fields[field_name].label = label
        return form


class DeleteIngredient(LoginRequiredMixin, ManagerRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'ingredient/delete_ingredient.html'
    success_url = '/stock/'

@login_required
@manager_required
def order(request, pk):
    ingredient = Ingredient.objects.get(pk = pk)
    ingredient.stock += ingredient.order_quantity
    ingredient.save()

    return redirect('/stock')
