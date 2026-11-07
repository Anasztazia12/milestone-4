from django.db.models import Prefetch
from django.db.models.functions import Lower
from django.shortcuts import render

from .models import Category, MenuItem


def menu_list(request):
    """Show every category with its available items."""
    available_items = MenuItem.objects.filter(
        is_available=True
    ).prefetch_related('allergens')

    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']

        if sortkey in ['name', 'price']:
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                available_items = available_items.annotate(
                    lower_name=Lower('name')
                )

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            available_items = available_items.order_by(sortkey)
            
    current_sorting = f'{sort}_{direction}'

    categories = Category.objects.prefetch_related(
        Prefetch('items', queryset=available_items, to_attr='available_items')
    )
    return render(request, 'menu/menu_list.html', {
        'categories': categories,
        'current_sorting': current_sorting,
    })

   