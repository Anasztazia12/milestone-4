from datetime import timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from menu.models import Category, MenuItem

from .forms import OrderForm
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


class CheckoutPageTests(TestCase):
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

    def put_dish_in_bag(self):
        session = self.client.session
        session['bag'] = {str(self.dish.pk): 2}
        session.save()

    def test_checkout_requires_login(self):
        response = self.client.get(reverse('checkout:checkout'))

        login_url = reverse('account_login')
        checkout_url = reverse('checkout:checkout')
        self.assertRedirects(response, f'{login_url}?next={checkout_url}')

    def test_empty_bag_redirects_to_menu(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('checkout:checkout'))

        self.assertRedirects(response, reverse('menu'))

    def test_checkout_page_shows_form_and_total(self):
        self.client.force_login(self.user)
        self.put_dish_in_bag()

        response = self.client.get(reverse('checkout:checkout'))

        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertContains(response, 'name="collection_time"')
        self.assertContains(response, 'Order total')


class OrderFormTests(TestCase):
    def form_data(self, minutes_from_now):
        collection_time = timezone.now() + timedelta(minutes=minutes_from_now)
        return {
            'full_name': 'Diner One',
            'phone_number': '07123456789',
            'collection_time': collection_time.strftime('%Y-%m-%dT%H:%M'),
        }

    def test_collection_time_in_one_hour_is_valid(self):
        form = OrderForm(data=self.form_data(60))
        self.assertTrue(form.is_valid())

    def test_collection_time_in_the_past_is_invalid(self):
        form = OrderForm(data=self.form_data(-60))
        self.assertFalse(form.is_valid())
        self.assertIn('collection_time', form.errors)

    def test_phone_number_is_required(self):
        data = self.form_data(60)
        data['phone_number'] = ''
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
