from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import *
from django.contrib.auth import authenticate, get_user_model, login
from crud_ajax.models import *




class AddAcctForm(forms.ModelForm):
    class Meta:
        model = t_acct
        fields = [
            'fname',
            ]
