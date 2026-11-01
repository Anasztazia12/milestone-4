from django.db.models import Prefetch
from django.shortcuts import render

from .models import Category, MenuItem


def menu_list(request):
    """Show every category with its available items."""
    available_items = MenuItem.objects.filter(
        is_available=True
    ).prefetch_related('allergens')
    categories = Category.objects.prefetch_related(
        Prefetch('items', queryset=available_items, to_attr='available_items')
    )
    return render(request, 'menu/menu_list.html', {'categories': categories})