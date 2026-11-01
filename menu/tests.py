from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

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

    def test_price_cannot_be_negative(self):
        self.item.price = Decimal('-1.00')
        with self.assertRaises(ValidationError):
            self.item.full_clean()
