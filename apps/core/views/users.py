from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# PROFILE VIEWS
def profile(request):
    user = request.user
    return render(request, 'user/users/profile.html', {
        'user': user
    })
