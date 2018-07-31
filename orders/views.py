from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import logout as logout_auth


@login_required
def home(request):
    return render(request, 'orders/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login_auth(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'orders/signup.html', {'form': form})

# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password1']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login_auth(request, user)
#         return redirect('home')
#     else:
#         form = UserCreationForm()
#         return render(request, 'orders/signup.html', {'form': form})

# def login_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login_auth(request, user)
#         return HttpResponseRedirect(reverse("signup"))
#     else:
#         return render(request, "orders/login.html", {"message": "Invalid credentials."})

def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() and user is not None:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login_auth(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'orders/login.html', {'form': form})

def logout_view(request):
    logout_auth(request)
    return render(request, "orders/login.html", {"message": "Logged out."})






# # Create your views here.
# def index(request):
#     return HttpResponse("Project 3: TODO")

# @login_required
# def home(request):
#     return render(request, 'home.html')
