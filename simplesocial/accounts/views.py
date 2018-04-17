from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name='accounts/signup.html'

    """ Lazy allows for the user to sign up, a simple reverse would redirect
        to the login page without taking their input """
