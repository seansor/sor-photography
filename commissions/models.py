from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CommissionOrder(models.Model):
    subject = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=1000)
    size = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=254, default="")
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.customer.id, self.subject)
        
class Quote(models.Model):
    order = models.OneToOneField(CommissionOrder, null=True, blank=True, on_delete=models.CASCADE)
    price_works = models.DecimalField(max_digits=6, decimal_places=2)
    price_travel = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    date = models.DateField()
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    
    def sum_price(self):
        self.price = self.price_works + self.price_travel
        return self.price
        
    def save(self, *args, **kwargs):
        if self.price_total != self.price_works + self.price_travel:
            self.price_total = self.sum_price()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return ("Id:{}, Value: €{}".format(self.id, self.price_total))
    