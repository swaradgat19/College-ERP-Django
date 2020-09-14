from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from auth import forms
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.   

class Login(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass


# Create your models here.
