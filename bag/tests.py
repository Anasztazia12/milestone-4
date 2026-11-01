from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from menu.models import Category, MenuItem


class BagPageTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Mains')
        self.dish = MenuItem.objects.create(
            category=category,
            name='Fish and chips',
            description='Classic pub meal',
            price=Decimal('12.50'),
            image='images/fish.jpg',
        )

    def test_empty_bag_page_loads(self):
        response = self.client.get(reverse('bag:view_bag'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
        self.assertContains(response, 'Your bag is empty.')

    def test_bag_page_shows_session_items_and_total(self):
        session = self.client.session
        session['bag'] = {str(self.dish.pk): 2}
        session.save()

        response = self.client.get(reverse('bag:view_bag'))

        self.assertContains(response, 'Fish and chips')
        self.assertContains(response, '£25.00')
        self.assertEqual(response.context['total'], Decimal('25.00'))
