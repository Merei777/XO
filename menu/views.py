from django.shortcuts import render, get_object_or_404
from .models import Category  
from .models import Dish

def menu_home(request):
    categories = Category.objects.prefetch_related('subcategories__dishes').all()
    return render(request, 'menu/menu.html', {'categories': categories})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'menu/dish_detail.html', {'dish': dish})