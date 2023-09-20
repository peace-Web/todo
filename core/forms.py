from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ["task_title", "completed"]

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]