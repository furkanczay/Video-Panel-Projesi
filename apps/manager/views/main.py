from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from apps.manager.models import GeneralSettings
from apps.manager.forms.site_settings import GeneralSettingsForm
from django.contrib import messages


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
