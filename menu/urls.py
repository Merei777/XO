from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_home, name='menu_home'),  # пример маршрута для меню
path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),]
