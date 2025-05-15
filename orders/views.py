# orders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from menu.models import Dish
from .forms import OrderForm

def home(request):
    """
    Простая информация о разделе заказов.
    Можно потом заменить на ваш шаблон или список прошлых заказов.
    """
    return HttpResponse("Это главная страница заказов.")

def add_to_cart(request, dish_id):
    """
    Добавить блюдо в корзину, хранимую в сессии.
    """
    dish = get_object_or_404(Dish, id=dish_id)
    cart = request.session.get('cart', {})
    # Увеличиваем количество на 1
    cart[str(dish_id)] = cart.get(str(dish_id), 0) + 1
    request.session['cart'] = cart

    messages.success(request, f"«{dish.name}» добавлено в корзину")
    # Возвращаем пользователя обратно на ту страницу, откуда он пришёл
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect(reverse('menu_home'))

def cart_view(request):
    """
    Показать текущее содержимое корзины:
    список блюд, их количество и итоговую сумму.
    """
    cart = request.session.get('cart', {})
    dishes = Dish.objects.filter(id__in=cart.keys())
    cart_items = []
    for dish in dishes:
        qty = cart.get(str(dish.id), 0)
        cart_items.append({
            'dish': dish,
            'quantity': qty,
            'subtotal': dish.price * qty,
        })
    total = sum(item['subtotal'] for item in cart_items)

    return render(request, 'orders/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })

def create_order(request):
    """
    Оформление заказа на основе формы OrderForm.
    После успешного создания — очищаем корзину и показываем страницу успеха.
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            # TODO: можно присвоить статус и адрес по умолчанию
            # Рассчитать total_price на основе корзины:
            cart = request.session.get('cart', {})
            dishes = Dish.objects.filter(id__in=cart.keys())
            total = sum(dish.price * cart.get(str(dish.id), 0) for dish in dishes)
            order.total_price = total
            order.save()

            # TODO: здесь создать OrderItem для каждого блюда из корзины

            # Очищаем корзину
            request.session['cart'] = {}

            messages.success(request, "Ваш заказ успешно оформлен!")
            return redirect('order_success')
        else:
            messages.error(request, "Проверьте корректность введённых данных.")
    else:
        form = OrderForm()

    return render(request, "orders/order_form.html", {"form": form})

def order_success(request):
    """
    Простая страница благодарности после оформления заказа.
    """
    return render(request, 'orders/order_success.html')
