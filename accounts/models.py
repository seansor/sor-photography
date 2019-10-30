from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserBillingInfo(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    remember_me = models.BooleanField(default=False)
    
    def __str__(self):
        return "{0}-{1}".format(self.id, self.full_name)

    