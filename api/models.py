from django.db import models
from django.conf import settings

class APIClient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='api_client')
    client_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"API Client: {self.client_name}"

class APILog(models.Model):
    client = models.ForeignKey(APIClient, on_delete=models.CASCADE, related_name='logs')
    endpoint = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    status_code = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    response_time = models.FloatField(help_text="Response time in seconds")

    def __str__(self):
        return f"Log for {self.client.client_name} on {self.endpoint}"

class APIKey(models.Model):
    client = models.ForeignKey(APIClient, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"API Key for {self.client.client_name}"

class APIRateLimit(models.Model):
    client = models.OneToOneField(APIClient, on_delete=models.CASCADE, related_name='rate_limit')
    max_requests_per_minute = models.PositiveIntegerField(default=60)

    def __str__(self):
        return f"Rate limit for {self.client.client_name}: {self.max_requests_per_minute} per minute"

class APIUsage(models.Model):
    client = models.ForeignKey(APIClient, on_delete=models.CASCADE, related_name='usage')
    date = models.DateField(auto_now_add=True)
    request_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Usage for {self.client.client_name} on {self.date}"
