from django.db import models
from products.models import ProductVariant
from accounts.models import UserBillingInfo

# Create your models here.

class OrderInfo(UserBillingInfo):
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    order_info = models.ForeignKey(OrderInfo, null=False, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    
    def sum_line_total(self):
        return self.quantity * self.product_variant.price
        
    def save(self, *args, **kwargs):
        if self.line_total != self.quantity * self.product_variant.price:
            self.line_total = self.sum_line_total()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product_variant.product.name, self.product_variant.price)