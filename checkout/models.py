from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVariant

# Create your models here.

class OrderInfo(models.Model):
    """ Order billing/shipping Information """
    customer = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    remember_me = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return "{}--{}".format(self.id, self.full_name)

class OrderLineItem(models.Model):
    """ Line Items for each order """
    order_info = models.ForeignKey(OrderInfo, null=False, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    # Set line_total to always be quantity * product price
    def sum_line_total(self):
        return self.quantity * self.product_variant.price

    def save(self, *args, **kwargs):
        if self.line_total != self.quantity * self.product_variant.price:
            self.line_total = self.sum_line_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product_variant.product.name,
                                      self.product_variant.price)
