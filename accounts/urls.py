from django.urls import path
from . import views


urlpatterns=[path("login/register/",views.register,name="register"),
             path("register/",views.register,name="register"),
             path("home/login/",views.login,name="login"),
             path("login/",views.login,name="login"),
             path("home/logout/",views.logout,name="logout"),
             path("home/recap/",views.recap,name="recap"),
             path('home/',views.home,name='home after login')]