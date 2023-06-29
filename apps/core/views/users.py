from django.shortcuts import render, redirect, get_object_or_404
from config.backends import PasswordlessAuthBackend
from apps.core.utils import send_otp
from apps.core.models import Users
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from apps.core.decorators import anonymous_required
from django.contrib import messages
from datetime import datetime
from apps.core.forms.users import UserUpdateForm
import pyotp


@anonymous_required()
def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = PasswordlessAuthBackend.authenticate(request, email=email)
        if user is not None:
            request.session['email'] = email
            subject = 'Giriş Onaylama Kodu'
            message = ' Giriş yapmak için gerekli kod: ' + send_otp(request)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('login_validate')
        else:
            messages.error(request, 'Bu eposta sistemde kayıtlı değil')
    return render(request, 'user/users/login.html', {})


@anonymous_required()
def login_validate(request):
    if request.method == 'POST':
        otp = request.POST['otp'].strip()
        email = request.session['email']

        otp_secret_key = request.session['otp_secret_key']
        otp_valid_date = request.session['otp_valid_date']

        if otp_secret_key and otp_valid_date is not None:
            valid_until = datetime.fromisoformat(otp_valid_date)

            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=300)
                if totp.verify(otp):
                    user = get_object_or_404(Users, email=email)
                    login(request, user, backend='config.backends.PasswordlessAuthBackend')
                    if request.session['otp_secret_key']:
                        del request.session['otp_secret_key']
                    if request.session['otp_valid_date']:
                        del request.session['otp_valid_date']

                    return redirect('homepage')
                else:
                    messages.error(request, 'Tek kullanımlık kod geçersiz!')
            else:
                messages.error(request, 'Tek kullanımlık kod zaman aşımına uğradı')
        else:
            messages.error(request, 'Tek kullanımlık kodda bir sorun var')
    return render(request, 'user/users/login_validate.html', context={})


@login_required()
# PROFILE VIEWS
def profile(request):
    user = request.user
    return render(request, 'user/users/profile.html', {
        'user': user
    })


@login_required()
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.save()
            messages.success(request, 'Profil bilgileriniz güncellendi')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'user/users/profile_edit.html', {
        'user': user,
        'form': form
    })
