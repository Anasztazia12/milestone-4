from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import OrderForm


@login_required
def checkout(request):
    """Show the checkout form with the customer's details filled in."""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is empty.')
        return redirect('menu')

    form = OrderForm(initial={
        'full_name': request.user.get_full_name(),
        'email': request.user.email,
    

    return render(request, 'checkout/checkout.html', {
        'form': form,
    })