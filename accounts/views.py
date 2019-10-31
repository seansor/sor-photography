from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .models import UserBillingInfo
from commissions.models import CommissionOrder, Quote

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

@login_required
def logout(request):
    """Log the user out"""
    
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
    number_of_quotes = quotes.count()
    quote_numbers = []
    for i in range(1, number_of_quotes+1):
        quote_numbers.append(str(i))
    quotes_zip = zip(quote_numbers, quotes)

    
    return render(request, 'profile.html', {'user': user, 'quotes': quotes, 'quotes_zip':quotes_zip})