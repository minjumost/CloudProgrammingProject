from django.shortcuts import render
from .models import Ingredient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .utils import update_expired, update_need_order_status
# Create your views here.


class ViewIngredients(ListView):
    model = Ingredient
    template_name = 'ingredient/list_ingredient.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        update_expired()
        update_need_order_status()
        return queryset
class CreateIngredient(CreateView):
    model = Ingredient
    fields = ['name', 'ammount', 'min_ammount', 'exp_date', ]
    template_name = 'ingredient/create_ingredient.html'
    success_url = '/stock/'

class UpdateIngredient(UpdateView):
    model = Ingredient
    fields = ['name', 'ammount', 'exp_date', 'min_ammount']
    success_url = '/stock/'
    template_name = 'ingredient/update_ingredient.html'

class DeleteIngredient(DeleteView):
    model = Ingredient
    template_name = 'ingredient/delete_ingredient.html'
    success_url = '/stock/'
