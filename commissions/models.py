from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quote(models.Model):
    price_works = models.DecimalField(max_digits=6, decimal_places=2)
    price_travel = models.DecimalField(max_digits=6, decimal_places=2)
    accepted = models.BooleanField(default=False)

class CommissionOrder(models.Model):
    description = models.TextField()
    size = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=254, default="")
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    quote = models.OneToOneField(Quote, default="1", on_delete=models.CASCADE)
    