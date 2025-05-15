# xo_lounge/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # админка
    path('admin/', admin.site.urls),

    # главная страница — сразу отдаём home.html
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # меню
    path('menu/', include('menu.urls')),

    # заказы
    path('orders/', include('orders.urls')),

    # оплаты
    path('payments/', include('payments.urls')),

    # API
    path('api/', include('api.urls')),

    # управление пользователями (регистрация, профиль и т.п.)
    path('users/', include('users.urls')),

    # стандартные пути для логина/логаута/пароля
    path('accounts/', include('django.contrib.auth.urls')),
]
