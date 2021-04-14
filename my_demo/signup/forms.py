# *_* coding: utf-8 *_*
# time:2021-04-1311:37
# tools:PyCharm
# file_name：forms.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
