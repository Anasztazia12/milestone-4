from decimal import Decimal

from django.shortcuts import render

from menu.models import MenuItem


def view_bag(request):
    """Display the menu items and quantities currently stored in the session."""
    bag = request.session.get('bag', {})
    items = MenuItem.objects.filter(pk__in=bag.keys()).order_by('name')
    bag_items = []
    total = Decimal('0.00')

    for item in items:
        quantity = bag.get(str(item.pk), 0)
        subtotal = item.price * quantity
        total += subtotal
        bag_items.append({
            'item': item,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'bag/bag.html', {
        'bag_items': bag_items,
        'total': total,
    })

# Create your views here.
