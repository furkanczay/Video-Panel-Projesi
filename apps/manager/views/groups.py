from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.admin import Group
from django.contrib import messages
from apps.manager.decorators import staff_login_required
from apps.manager.forms.groups import *


@staff_login_required
def groups_page(request):
    groups = Group.objects.all().order_by('-id')
    return render(request, 'manager/groups/list.html', context={
        'groups': groups
    })


@staff_login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grup Başarıyla Eklendi')
            return redirect('admin_groups_page')
    else:
        form = GroupCreateForm()
    return render(request, 'manager/groups/create.html', context={
        'form': form
    })


@staff_login_required
def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grup başarıyla güncellendi')
            return redirect('admin_groups_page')
    else:
        form = GroupUpdateForm(instance=group)
    return render(request, 'manager/groups/update.html', context={
        'form': form,
        'group': group
    })


@staff_login_required
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if group.name == 'Öğrenci' or group.name == 'Eğitmen' or group.name == 'Personel' or group.name == 'Yönetici':
        messages.error(request, 'Ana grupları silemezsiniz')
        return redirect('admin_groups_page')
    else:
        group = group.delete()
        if group:
            messages.success(request, 'Grup Başarıyla Silindi')
            return redirect('admin_groups_page')
