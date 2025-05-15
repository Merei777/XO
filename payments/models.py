from django.db import models
from orders.models import Order

class PaymentGateway(models.Model):
    name = models.CharField(max_length=100, unique=True)
    api_endpoint = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    gateway = models.ForeignKey(PaymentGateway, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)
    reference_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Transaction for Order #{self.order.id}"

class Refund(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='refunds')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"Refund for Transaction #{self.transaction.id}"

class PaymentLog(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='logs')
    log_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for Transaction #{self.transaction.id}"

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=100, unique=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice #{self.invoice_number} for Order #{self.order.id}"
