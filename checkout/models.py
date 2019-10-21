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
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product_variant.product.name, self.product_variant.price)