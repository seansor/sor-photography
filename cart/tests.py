from django.test import TestCase, Client

# Create your tests here.

class CartViewsTest(TestCase):
    """ Testing of cart views """
    
    def setUp(self):
        # Setup client.
        self.client = Client()
        #self.user = User.objects.create_user(username="JohnDoe", password="password")
        
        
    def test_view_cart_client(self):
        # Issue a GET request.
        response = self.client.get('/cart/')
        
        # Verify that response is 200 OK.
        self.assertEqual(response.status_code, 200)
        
    def test_add_cart_client(self):
        # Issue a GET request.
        response = self.client.get('/cart/')
        
        # Check that request redirects to cart/<product_id> before rendering login
        # then the response is 200 OK.
        self.assertRedirects(response, "/login/", status_code=301,
                            target_status_code=200, fetch_redirect_response=True)