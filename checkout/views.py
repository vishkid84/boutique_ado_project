from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context ={
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HOVTSCOjJj6pV2785uP1zZ0luTTwGWp2sJ14RMhJKHr0A2SFjdNdDzCPJkL1KBWEPeIz5KIC4RLAeeNy2f59Ezi00Oq7UYnPw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)