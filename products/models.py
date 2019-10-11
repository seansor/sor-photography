from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=254, default="")
    current_series = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=254, default="")
    location = models.CharField(max_length=254, default="")
    collection = models.ForeignKey(Collection, default="1", on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return ("{}, {}".format(self.name, self.location))

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=254, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return ("{} @ {}".format(self.size, self.price))
    
