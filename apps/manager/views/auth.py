from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    elif request.user.is_authenticated and not request.user.is_staff:
        messages.error(request, 'Bu sayfaya erişim izniniz bulunmuyor!')
        return redirect('homepage')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            if not user.is_staff:
                messages.error(request, 'Bu sayfaya erişim izniniz bulunmuyor!')
                return redirect('homepage')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre!')
            return redirect('admin_login')
    return render(request, 'manager/auth/login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')
