from django.test import TestCase
from .models import Product

# Create your tests here.
class productTests(TestCase):
    """
    Tests to be run against product
    models
    """
    
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')