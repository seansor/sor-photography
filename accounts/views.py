from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .models import UserBillingInfo
from .forms import BillingForm
from commissions.models import CommissionOrder, Quote

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

@login_required
def logout(request):
    """Log the user out"""
    
    # if not request.user.is_authenticated:
    #     request.session.set_expiry(0)
    auth.logout(request)
    messages.success(request, "You have succesfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """Return login page"""
    # This is the decorator that prevents a user from getting access to a page
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
        if user:
            auth.login(user=user, request=request)
            messages.success(request, "You have successfully logged in!")
            request.session.set_expiry(None)
            return redirect(reverse('index'))
        else:
            login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    
    
    return render(request, 'login.html', {"login_form": login_form})

    
def register(request):
    """Render registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
            
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html',
        {'registration_form': registration_form})
        

def user_profile(request):
    """The user's profile page"""
    
    user = request.user
    quotes = Quote.objects.filter(order__customer=user.id)
    quote_numbers = ['One', 'Two', 'Three', 'Four', 'Five']
    quotes_zip = zip(quote_numbers, quotes)
    
    if request.method == 'POST':
        try:
            billing_info = get_object_or_404(UserBillingInfo, customer=user)
            billing_form = BillingForm(request.POST, instance=billing_info)
            if billing_form.is_valid():
                user_billing_info = billing_form.save(commit=False)
                user_billing_info.customer = request.user
                user_billing_info.remember_me = True
                user_billing_info.save()
                return redirect(reverse('profile'))
        except:
            user_billing_info = billing_form.save(commit=False)
            user_billing_info.customer = request.user
            user_billing_info.remember_me = True
            user_billing_info.save()
            return redirect(reverse('profile'))

    try:
        billing_info = UserBillingInfo.objects.get(customer=user)
        logger.info(billing_info)
        
        billing_form = BillingForm(initial={'full_name': billing_info.full_name, 
                                        'phone_number': billing_info.phone_number,
                                        'country': billing_info.country,
                                        'postcode': billing_info.postcode,
                                        'town_or_city': billing_info.town_or_city,
                                        'street_address1': billing_info.street_address1,
                                        'street_address2': billing_info.street_address2,
                                        'county': billing_info.county
                                        })
    except:
        billing_form = BillingForm()
    
    return render(request, 'profile.html', {'user': user, 'billing_form': billing_form, 'quotes': quotes, 'quotes_zip':quotes_zip})
    