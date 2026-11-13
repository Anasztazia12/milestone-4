from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Order


class OrderForm(forms.ModelForm):
    """Contact details and collection time for an order."""

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number', 'collection_time']
        widgets = {
            'collection_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['collection_time'].required = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_collection_time(self):
        """The kitchen needs at least 60 minutes to cook the food."""
        collection_time = self.cleaned_data['collection_time']
        earliest = timezone.now() + timedelta(minutes=60)
       