from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
@unittest.skipIf(os.environ.get('TRAVIS') == 'true', 'Skipping this test on Travis CI.')
class CommissionViewsTest(TestCase):
    """ Testing of cart views """
    
    def setUp(self):
        # Setup client.
        self.client = Client()
        self.user = User.objects.create_user(username="JohnDoe", password="password")
        
    def test_create_order_client_for_logged_in_user(self):
        # Login User
        self.client.login(username="JohnDoe", password="password")
        # Issue a GET request.
        response = self.client.get('/commissions/create_order/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_orders_client_for_logged_in_user(self):
        # Login User
        self.client.login(username="JohnDoe", password="password")
        # Issue a GET request.
        response = self.client.get('/commissions/orders/')
        self.assertEqual(response.status_code, 200)
