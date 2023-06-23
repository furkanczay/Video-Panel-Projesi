from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# AUTHENTICATION VIEWS
def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, _('Böyle bir kullanıcı bulunamadı'))
    return render(request, 'user/users/login.html')


@login_required()
def logout_page(request):
    logout(request)
    return redirect('login')

# PROFILE VIEWS
