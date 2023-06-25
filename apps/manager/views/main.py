from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from apps.manager.models import GeneralSettings
from apps.manager.forms.site_settings import GeneralSettingsForm
from django.contrib import messages
from apps.core.models import Users
from django.contrib.auth.admin import AdminPasswordChangeForm


@staff_member_required()
def dashboard(request):
    return render(request, 'manager/main/dashboard.html', {})


@staff_member_required()
def general_settings(request):
    general_settings_objects = GeneralSettings.objects.first()
    if request.method == 'POST':
        form = GeneralSettingsForm(request.POST, request.FILES, instance=general_settings_objects)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genel ayarlar başarıyla güncellendi')
    else:
        form = GeneralSettingsForm(instance=general_settings_objects)
    return render(request, 'manager/main/general_settings.html', {
        'form': form
    })


@login_required()
@staff_member_required()
def user_update_password(request, pk):
    user = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdminPasswordChangeForm(user=user)
    return render(request, 'manager/main/user_update_password.html', context={
        'user': user,
        'form': form
    })
