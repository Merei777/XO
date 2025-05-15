from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Предположим, мы хотим выбрать только адрес доставки.
        # Остальные поля, такие как статус или общая стоимость,
        # могут вычисляться автоматически.
        fields = ['delivery_address']
