import os
from django.conf import settings
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Product, Collection

# Create your tests here.

class CartViewsTest(TestCase):
    """ Testing of cart views """
    
    def setUp(self):
        # Setup client.
        self.client = Client()
        
        # Create Collection
        self.collection=Collection.objects.create(name="collection", current_series=True)
        
        # Create Image upload for Product
        file_path = os.path.join(settings.BASE_DIR, "static/", "img/" , "camera-logo.jpg")
        self.img = SimpleUploadedFile(name='camera-logo.jpg',
                                      content=open(file_path, 'rb').read(), content_type='image/jpg')           
        
        # Create Product
        self.product = Product.objects.create(pk=2, name="photo", location="dublin",
                                              collection=self.collection,
                                              description="New Photo", image=self.img)
        
        
    def test_view_cart_client(self):
        # Issue a GET request.
        response = self.client.get('/cart/')
        
        # Verify that response is 200 OK.
        self.assertEqual(response.status_code, 200)
        
    def test_add_product_id_2_to_cart(self):
        # Issue a GET request.
        response = self.client.get('/cart/add/2')
        
        # Check that request gets cart/add/<product_id> and then the response is 200 OK.
        self.assertEqual(response.status_code, 200)
