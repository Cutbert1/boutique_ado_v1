from django.shortcuts import render, redirect, reverse
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
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RAA2e4Gn0n89g1X6vHcxhQysQAWHOzQSMHPKoIGBZcYFIwq9Yy09XtmMl2FOL4dWLCm2MISYDOnH9bpFHelqGlS00TrFqdreF',  # noqa
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
