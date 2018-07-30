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
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout")
]

    # path('', orders_views.signup, name='signup'),
    # path("admin/", admin.site.urls),
    # url(r'^$', orders_views.home, name='home'),
    # # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    # url(r'^signup/$', orders_views.signup, name='signup'),