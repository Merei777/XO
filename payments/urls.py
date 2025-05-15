from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='payments_home'),
   #  path('create/', views.create_order, name='create_order'),
]
