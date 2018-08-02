from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *

@login_required
def home(request):
    messages.success(request, "You have successfully logged in.")
    menu = {
        "toppings": Topping.objects.all(),
        "regpizza": RegPizza.objects.all(),
        "sicilian": SicilianPizza.objects.all(),
        "subs": Subs.objects.all(),
        "pasta": Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinner": DinnerPlatter.objects.all(),
    }
    return render(request, 'orders/home.html', menu)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login_auth(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'orders/signup.html', {'form': form})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_auth(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        messages.error(request, "Invalid username or password. Please try again.")
        return render(request, 'orders/login.html')

def loginred(request):
    return render(request, 'orders/login.html')

def logout_view(request):
    logout_auth(request)
    return render(request, "orders/login.html")
    messages.info(request, "You have successfully logged out.")


def logoutred(request):
    return render(request, 'orders/login.html')