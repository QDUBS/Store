from django.shortcuts import render, redirect
from Store.models import Item
from .forms import ProfileForm, Form
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datetime import date
from django.utils import timezone
import datetime
from django.contrib import messages

# Create your views here.


def Register(request):
    if request.method == 'POST':
        form = Form(request.POST)
        profileForm = ProfileForm(request.POST)

        if form.is_valid() and profileForm.is_valid():
            user = form.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully')
        return redirect('register')
    else:
        form = Form()
        profileForm = ProfileForm()
    
    return render(request, 'registration/register.html', {'form': form, 'profileform': profileForm})
