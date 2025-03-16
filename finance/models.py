from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Essentials', 'Essentials'),
        ('Wants', 'Wants'),
        ('Investments', 'Investments'),
        ('Savings', 'Savings'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    description = models.TextField()
    source = models.CharField(max_length=20, choices=[('UPI', 'UPI'), ('SMS', 'SMS'), ('Manual', 'Manual')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.category}"