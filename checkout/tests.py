from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from menu.models import Category, MenuItem

from .models import Order, OrderLineItem


class OrderTotalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='diner', password='test-pass-123'
        )
        category = Category.objects.create(name='Mains')
        self.dish = MenuItem.objects.create(
            category=category,
            name='Fish and chips',
            description='Classic pub meal',
            price=Decimal('12.50'),
            image='images/fish.jpg',
        )

    def test_update_total_sums_line_items(self):
        order = Order.objects.create(user=self.user, full_name='Diner One')
        OrderLineItem.objects.create(order=order, menu_item=self.dish, quantity=2)

        order.update_total()

        self.assertEqual(order.total, Decimal('25.00'))

    def test_order_number_is_generated_on_save(self):
        order = Order.objects.create(user=self.user, full_name='Diner One')

        self.assertTrue(order.order_number)

    def test_new_order_status_is_received(self):
        order = Order.objects.create(user=self.user, full_name='Diner One')

        self.assertEqual(order.status, 'received')
