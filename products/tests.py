from django.test import TestCase
from .models import Product

# Create your tests here.
@unittest.skipIf(os.environ.get('TRAVIS') == 'true', 'Skipping this test on Travis CI.')
class productTests(TestCase):
    """
    Tests to be run against product
    models
    """
    
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name.name), 'A Product')