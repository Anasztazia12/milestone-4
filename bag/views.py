from decimal import Decimal

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from menu.models import MenuItem


@require_POST
def add_to_bag(request, item_id):
    """Add the requested quantity of an available menu item to the session bag."""
    item = get_object_or_404(MenuItem, pk=item_id, is_available=True)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 0

    if quantity < 1 or quantity > 99:
        messages.error(request, 'Choose a quantity between 1 and 99.')
        return redirect('menu')

    bag = request.session.get('bag', {})
    item_key = str(item.pk)
    bag[item_key] = bag.get(item_key, 0) + quantity
    request.session['bag'] = bag
    messages.success(request, f'{item.name} added to your bag.')
    return redirect('menu')


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

