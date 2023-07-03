from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import stripe
from .models import StripeCustomer
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .forms import UserCreationFormWithEmail
from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django import forms

stripe.api_key = 'sk_test_51NLrpZHM16YgbOmpEsBLGZhHvfm2uPFKjunk0ORes1OAw0phBVameYTXcWxaGXzOoV1B0iCu1nBN6onMsEWjUTm600zUlLeynf'

# Create your views here.
@login_required
def settings(request):
    membership = False
    cancel_at_period_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)
        subscription.cancel_at_period_end = True
        request.user.customer.cancel_at_period_end = True
        cancel_at_period_end = True
        subscription.save()
        request.user.customer.save()
    else:
        try:
            if request.user.customer.membership:
                membership = True
            if request.user.customer.cancel_at_period_end:
                cancel_at_period_end = True
        except StripeCustomer.DoesNotExist:
            membership = False
    return render(request, 'registration/settings.html', {'membership':membership,
    'cancel_at_period_end':cancel_at_period_end})

def join(request):
    return render(request, 'registration/join.html')

def success(request):
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
        customer = StripeCustomer()
        customer.user = request.user
        customer.stripeid = session.customer
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = session.subscription
        customer.save()
    return render(request, 'membership/success.html')

def cancel(request):
    return render(request, 'membership/cancel.html')

@login_required
def checkout(request):

    try:
        if request.user.stripecustomer.registration:
            return redirect('settings')
    except StripeCustomer.DoesNotExist:
        pass

    if request.method == 'POST':
        pass
    else:
        registration = 'monthly'
        final_dollar = 102.08
        membership_id = 'price_1NORWMHM16YgbOmpc5zgroU7'
        if request.method == 'GET' and 'membership' in request.GET:
            if request.GET['membership'] == 'yearly':
                registration = 'yearly'
                membership_id = 'price_1NLsWSHM16YgbOmpb3rpckjd'
                final_dollar = 1020.80

        # Create Strip Checkout
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email = request.user.email,
            line_items=[{
                'price': membership_id,
                'quantity': 1,
            }],
            mode='subscription',
            allow_promotion_codes=True,
            success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cancel',
        )

        return render(request, 'membership/checkout.html', {'final_dollar': final_dollar, 'session_id': session.id})


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy ('login') + '?register'
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        # modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form
    
