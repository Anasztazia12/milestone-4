from decimal import Decimal

from menu.models import MenuItem


def bag_contents(request):
    """Make the bag total and item count available on every page."""
    bag = request.session.get('bag', {})
    bag_total = Decimal('0.00')
    bag_count = 0

    for item in MenuItem.objects.filter(pk__in=bag.keys()):
        quantity = bag[str(item.pk)]
        bag_total += item.price * quantity
        bag_count += quantity

    return {
        'bag_total': bag_total,
        'bag_count': bag_count,
    }
