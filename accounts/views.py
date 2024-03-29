from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from checkout.models import OrderLineItem
from commissions.models import Quote


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

    return render(request, 'registration.html', {'registration_form': registration_form})


def user_profile(request):
    """The user's profile page"""

    user = request.user
    quotes = Quote.objects.filter(order__customer=user.id)
    order_history = OrderLineItem.objects.filter(order_info__customer=user.id).order_by('-order_info__date')

    return render(request, 'profile.html', {'user': user, 'quotes': quotes, 'order_history': order_history})
