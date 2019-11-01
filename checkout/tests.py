from datetime import datetime
import os
from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Product, ProductVariant, Collection
from .models import OrderInfo, OrderLineItem


# Create your tests here.

class OrderInfoTest(TestCase):
    """ Testing of OrderInfo model """
    
    def setUp(self):
        self.user = User.objects.create_user(username="JohnDoe", password="password")
        
        self.order_info = OrderInfo.objects.create(customer=self.user, full_name="John Doe",
                                                   phone_number="0851234567", street_address1="New Street",
                                                   street_address2="New Street 2",town_or_city="Dublin",
                                                   county="Dublin", country="Ireland", postcode="D12345",
                                                   remember_me=True, date=timezone.now())


    def test_customer_is_current_user(self):
        """Current User is correctly identified as customer"""
        self.assertEqual(self.order_info.customer, self.user)
    
        
    def test_order_info_has_fullname(self):
        # OrderInfo.full_name correctly identified
        order_info = OrderInfo.objects.get(full_name="John Doe")
        self.assertEqual(order_info.full_name, "John Doe")
    
        
    def test_to_check_order_date_is_current_date(self):
        # Check that timestamp correctly adds current time to Order
        order_info = OrderInfo.objects.get(full_name="John Doe")
        order_time = order_info.date
        current_time = datetime.now().date()
        self.assertAlmostEqual(order_time, current_time)
        
        
class OrderLineItemTest(TestCase):
    """ Testing of OrderLineItem Model """
    
    def setUp(self):
        # Create User
        self.user = User.objects.create_user(username="JohnDoe", password="password")
        
        # Create OrderInfo
        self.order_info = OrderInfo.objects.create(customer=self.user, full_name="John Doe",
                                                   phone_number="0851234567", street_address1="New Street",
                                                   street_address2="New Street 2", town_or_city="Dublin",
                                                   county="Dublin", country="Ireland", postcode="D12345",
                                                   remember_me=True, date=timezone.now())
        
        # Create Collection
        self.collection=Collection.objects.create(name="collection", current_series=True)
        
        # Create Image upload for Product
        file_path = os.path.join(settings.BASE_DIR, "static/", "img/" , "camera-logo.jpg")
        self.img = SimpleUploadedFile(name='camera-logo.jpg',
                                      content=open(file_path, 'rb').read(), content_type='image/jpg')           
        
        # Create Product
        self.product = Product.objects.create(name="photo", location="dublin",
                                              collection=self.collection,
                                              description="New Photo", image=self.img)
         
        # Create 2 product variants                      
        self.product_variant_1 = ProductVariant.objects.create(product=self.product,
                                                               size="120mmx240mm",
                                                               price=35.00)
        self.product_variant_2 = ProductVariant.objects.create(product=self.product,
                                                               size="240mmx480mm",
                                                               price=70.00)
        
        # Create 2 order line items with different product variant                     
        self.order_line_1 = OrderLineItem.objects.create(order_info=self.order_info,
                                                         product_variant=self.product_variant_1,
                                                         quantity=2, line_total=70)
                                     
        self.order_line_2 = OrderLineItem.objects.create(order_info=self.order_info,
                                                         product_variant=self.product_variant_2,
                                                         quantity=2, line_total=140)
                                     
        
    def test_order_line_1_order_info(self):
        """Test if order_info in order_line_1 matches order_info"""
        self.assertEqual(self.order_info, self.order_line_1.order_info)
        
    def test_order_line_2_order_info(self):
        """Test if order_info in order_line_2 matches order_info"""
        self.assertEqual(self.order_info, self.order_line_2.order_info)
        
    def test_order_line_1_product_variant(self):
        """Test if product_variant in order_line_1 matches created product_variant_1"""
        self.assertEqual(self.product_variant_1, self.order_line_1.product_variant)
        
    def test_order_line_2_product_variant(self):
        """Test if product_variant in order_line_2 matches created product_variant_1"""
        self.assertEqual(self.product_variant_2, self.order_line_2.product_variant)
    


class CheckoutViewsTest(TestCase):
    """ Testing of checkout views """
    
    def setUp(self):
        # Setup client.
        self.client = Client()
        self.user = User.objects.create_user(username="JohnDoe", password="password")
        
        
    def test_checkout_client_logged_in(self):
        # Login User and issue a GET request.
        self.client.login(username="JohnDoe", password="password")
        response = self.client.get('/checkout')
        
        # Verify that login authentication is checked before rendering checkout
        # with the response is 200 OK.
        self.assertRedirects(response, "/checkout/", status_code=301,
                            target_status_code=200, fetch_redirect_response=True)

        
    def test_checkout_client_logged_out(self):
        # Issue a GET request.
        response = self.client.get('/checkout', follow=True)
        
        # Check that request redirects to login before rendering checkout
        # then the response is 200 OK.
        self.assertRedirects(response, "/accounts/login/?next=/checkout/", status_code=301)