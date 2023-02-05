from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('publishRide', views.publishRide, name="publishRide"),
    path('search', views.search, name="search"),
    path('signout', views.signout, name="signout"),
]