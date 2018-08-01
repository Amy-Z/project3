from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


@login_required
def home(request):
    messages.success(request, "You have successfully logged in.")
    return render(request, 'orders/home.html')

# def home(request):
#     if not request.user.is_authenticated:
#         return render(request, "orders/login.html", {"message": None})
#     context = {
#         "order": request.order
#     }
#     return render(request, "orders/home.html", context)


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
        return render(request, 'orders/login.html', {"message": "Invalid credentials."})

def loginred(request):
    return render(request, 'orders/login.html')

def logout_view(request):
    messages.info(request, "You have successfully logged out.")
    logout_auth(request)
    return render(request, "orders/signup.html")

# def login_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login_auth(request, user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#         return render(request, 'orders/home.html', {'form': form})
