from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from zoo_shop_app.models import ShoppingCart, Sales
from zoo_shop_app.forms import AddressForm


class OrderViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')
        self.client.force_login(self.user)
        self.cart_item = ShoppingCart.objects.create(client=self.user.client, product='Product 1', quantity=2)

    def test_create_order_view(self):
        response = self.client.get(reverse('create_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_cart/enter_address.html')

        form_data = {'address': 'Test Address'}
        response = self.client.post(reverse('create_order'), form_data)
        self.assertEqual(response.status_code, 302)

        self.assertTrue(Sales.objects.filter(client=self.user.client).exists())
        self.assertFalse(ShoppingCart.objects.filter(client=self.user.client).exists())

    def test_order_confirmation_view(self):
        order = Sales.objects.create(client=self.user.client, total_cost=100, address='Test Address')
        response = self.client.get(reverse('order_confirmation', kwargs={'order_id': order.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_cart/order_confirmation.html')
