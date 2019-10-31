from django.test import TestCase, Client
from .models import OrderInfo, OrderLineItem
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your tests here.

class OrderTestCase(TestCase):
    """ Testing of checkout models """
    
    def setUp(self):
        user = User.objects.create_user(username="JohnDoe", password="password")
        
        OrderInfo.objects.create(customer=user, full_name="John Doe", phone_number="0851234567",
                                street_address1="New Street", street_address2="New Street 2",
                                town_or_city="Dublin", county="Dublin", country="Ireland",
                                postcode="D12345", remember_me=True, date=timezone.now())
        
        # order_info = OrderInfo.objects.get(full_name="John Doe")
                                
        # OrderLineItem.objects.create(order_info=order_info, product_variant=product_variant, quantity=2, line_total=sum_line_total())
        
        
        # def sum_line_total(self):
        # return self.quantity * self.product_variant.price
        
        # def save(self, *args, **kwargs):
        #     if self.line_total != self.quantity * self.product_variant.price:
        #         self.line_total = self.sum_line_total()
        #     super().save(*args, **kwargs)
 

    def test_customer_is_current_user(self):
        """Current User is correctly identified as customer"""
        order_info = OrderInfo.objects.get(full_name="John Doe")
        user = User.objects.get(username="JohnDoe")
        self.assertEqual(order_info.customer, user)
    
        
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