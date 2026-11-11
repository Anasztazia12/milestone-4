from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['position', 'name']

    def __str__(self):
        return self.name


class Allergen(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='items'
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
    )
    image = models.CharField(max_length=100)
    is_vegetarian = models.BooleanField(default=False)
    is_baby_friendly = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    allergens = models.ManyToManyField(
        Allergen, blank=True, related_name='items'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
