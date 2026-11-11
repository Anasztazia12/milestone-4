import uuid
from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from menu.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
    ]

    order_number = models.CharField(max_length=32, unique=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
    )
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, default='')
    collection_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='received'
    )
    stripe_pid = models.CharField(max_length=254, blank=True, default='')
    total = models.DecimalField(
        max_digits=6, decimal_places=2, default=Decimal('0.00')
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total = self.lineitems.aggregate(
            models.Sum('lineitem_total')
        )['lineitem_total__sum'] or Decimal('0.00')
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='lineitems'
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, editable=False
    )

    def save(self, *args, **kwargs):
        self.lineitem_total = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.menu_item.name} x {self.quantity}'
