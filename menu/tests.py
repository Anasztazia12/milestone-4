from decimal import Decimal

from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Allergen, Category, MenuItem


class MenuModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Mains')
        self.milk = Allergen.objects.create(name='Milk')
        self.item = MenuItem.objects.create(
            category=self.category,
            name='Fish and Chips',
            description='Crispy battered cod with chunky chips.',
            price=Decimal('14.50'),
            image='images/fish-and-chips.jpg',
        )

    def test_string_names(self):
        self.assertEqual(str(self.category), 'Mains')
        self.assertEqual(str(self.milk), 'Milk')
        self.assertEqual(str(self.item), 'Fish and Chips')

    def test_item_is_not_vegetarian_by_default(self):
        self.assertFalse(self.item.is_vegetarian)

    def test_item_is_available_by_default(self):
        self.assertTrue(self.item.is_available)

    def test_item_can_have_allergens(self):
        self.item.allergens.add(self.milk)
        self.assertIn(self.milk, self.item.allergens.all())

    def test_ingredients_are_empty_by_default(self):
        self.assertEqual(self.item.ingredients, '')

    def test_item_can_store_ingredients(self):
        self.item.ingredients = 'Cod, flour, potatoes'
        self.item.full_clean()
        self.assertEqual(self.item.ingredients, 'Cod, flour, potatoes')

    def test_price_cannot_be_negative(self):
        self.item.price = Decimal('-1.00')
        with self.assertRaises(ValidationError):
            self.item.full_clean()


class MenuFixtureTests(TestCase):
    fixtures = ['menu.json']

    def test_fixture_loads_menu_items(self):
        self.assertEqual(MenuItem.objects.count(), 30)

    def test_every_item_has_an_existing_image(self):
        for item in MenuItem.objects.all():
            self.assertIsNotNone(finders.find(item.image), item.image)


class MenuPageTests(TestCase):
    fixtures = ['menu.json']

    def test_menu_page_loads(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_list.html')

    def test_categories_follow_menu_order(self):
        response = self.client.get(reverse('menu'))
        names = [category.name for category in response.context['categories']]
        self.assertEqual(names[0], 'Starters')
        self.assertEqual(names[-1], 'Desserts')
        self.assertIn('Kids Menu', names)

    def test_page_shows_prices_and_allergens(self):
        response = self.client.get(reverse('menu'))
        self.assertContains(response, '£15.50')
        self.assertContains(response, 'Cereals containing gluten')

    def test_vegetarian_items_are_labelled(self):
        response = self.client.get(reverse('menu'))
        self.assertContains(response, 'Vegetarian Burger')
        self.assertContains(response, 'text-bg-success')

    def test_baby_friendly_items_are_labelled(self):
        response = self.client.get(reverse('menu'))
        self.assertContains(response, 'Baby friendly</span>', count=5)

    def test_unavailable_items_are_hidden(self):
        MenuItem.objects.filter(name='Beef Steak').update(is_available=False)
        response = self.client.get(reverse('menu'))
        self.assertNotContains(response, 'Beef Steak')

    def test_main_navigation_links_to_menu(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, reverse('menu'))

    def test_menu_sorts_by_price_low_to_high(self):
        response = self.client.get(reverse('menu') + '?sort=price&direction=asc')

        for category in response.context['categories']:
            prices = [item.price for item in category.available_items]
            self.assertEqual(prices, sorted(prices))

    def test_unknown_sort_does_not_break_menu(self):
        response = self.client.get(reverse('menu') + '?sort=wrong')
        self.assertEqual(response.status_code, 200)
