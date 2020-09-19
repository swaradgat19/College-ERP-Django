from django.forms import ModelForm
from main import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Attendance_Form(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']