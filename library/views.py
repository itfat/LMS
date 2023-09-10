# from django.contrib.auth.views import LoginView
# from library.forms import MyAuthenticationForm
# from django.urls import reverse, reverse_lazy

# from user.models import MyUser
# from django.contrib.auth import authenticate, login
# from django import forms

# from django.contrib.auth.views import LoginView

# from user.models import MyUser
# import logging

# logger = logging.getLogger(__name__)

# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'
#     authentication_form = MyAuthenticationForm  # Replace with your custom authentication form

#     def form_valid(self, authentication_form):
#         email = authentication_form.cleaned_data["email"]
#         password = authentication_form.cleaned_data["password"]
#         user = authenticate(username=email, password=password)

#         if user is not None:
#             login(self.request, user)
#             logger.info("User logged in successfully: %s", user)
#             return super().form_valid(authentication_form)
#         else:
#             logger.warning("Failed login attempt for user: %s", user)
#             raise forms.ValidationError("Invalid username or password.")

#     def get_success_url(self):
#         return reverse('books')

from rest_framework import generics
from user.forms import SignUpForm
from user.models import MyUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView


class UserView(DetailView):
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

    


