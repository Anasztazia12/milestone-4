from django.contrib import admin

from .models import Allergen, Category, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_vegetarian', 'is_available')
    list_filter = ('category', 'is_vegetarian', 'is_available')
    search_fields = ('name', 'description')
    filter_horizontal = ('allergens',)


admin.site.register(Category)
admin.site.register(Allergen)
