# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.signup, name='signup'),
# ]


from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from orders import views as orders_views

from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_view, name="login"),
    path("loginred", views.loginred, name="loginred"),
    path("logout", views.logout_view, name="logout"),
    path("logoutred", views.logoutred, name="logoutred"),
    path("cart/<type_pizza>/<pizza>", views.shoppingcart, name="cart")
]
