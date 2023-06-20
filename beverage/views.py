from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from management.utils import manager_required
from .models import Beverage, Recipt, Ingredient
from django.apps import apps
from django.shortcuts import redirect

# Create your views here.

class BeverageList(ListView):
    model = Beverage
    template_name = 'beverage/menu.html'

class BeverageDetail(LoginRequiredMixin, DetailView):
    model = Beverage
    template_name = 'beverage/recipt.html'
    context_object_name = 'beverage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the Recipt data related to the Beverage
        context['recipts'] = Recipt.objects.filter(beverage__id=self.object.id)
        return context

@login_required
@manager_required
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        ingredients = request.POST.getlist('ingredients')
        image = request.FILES.get('image')

        # Beverage 모델에 데이터 저장
        beverage = Beverage(name=name, price=price, image=image)
        beverage.save()
        beverage.ingredients.set(ingredients)
        return redirect('/menu/create_recipt/{}'.format(beverage.pk))

    Ingredient = apps.get_model('ingredient', 'Ingredient')
    ingredients = Ingredient.objects.all()
    return render(
        request,
        'beverage/new_beverage.html',
        {
            'ingredients': ingredients,
        }
    )
@login_required
@manager_required
def create_recipt(request, pk):
    beverage = Beverage.objects.get(pk=pk)

    if request.method == 'POST':
        quantities = {}

        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                ingredient_name = key.split('quantity_')[1]
                quantities[ingredient_name] = value

        for ingredient_name, quantity in quantities.items():
            ingredient = Ingredient.objects.get(name=ingredient_name)
            recipt = Recipt.objects.get(beverage=beverage, ingredients=ingredient)
            recipt.quantity = quantity
            recipt.save()
        print(f"Saved Recipt: beverage={recipt.beverage}, ingredient={recipt.ingredients}, quantity={recipt.quantity}")
        return redirect('/menu/')

    recipt = Recipt.objects.filter(beverage=beverage)
    return render(
        request,
        'beverage/new_recipt.html',
        {
            'recipt':recipt,
        }
    )

@login_required
@manager_required
def update_beverage(request, pk):
    beverage = Beverage.objects.get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        ingredients = request.POST.getlist('ingredients')
        image = request.FILES.get('image')

        if name:
            beverage.name = name
        if price:
            beverage.price = price
        if image:
            beverage.image = image
        if ingredients:
            beverage.ingredients.set(ingredients)
        beverage.save()

        return redirect('/menu/create_recipt/{}'.format(beverage.pk))

    Ingredient = apps.get_model('ingredient', 'Ingredient')
    ingredients = Ingredient.objects.all()
    return render(
        request,
        'beverage/update_beverage.html',
        {
            'beverage': beverage,
            'ingredients': ingredients,
        }
    )
@login_required
@manager_required
def delete_beverage(request, pk):
    beverage = Beverage.objects.get(pk=pk)
    beverage.delete()
    return redirect('/menu/')