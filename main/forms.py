from django import forms
from main import models


class Attendance_Form(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = '__all__'