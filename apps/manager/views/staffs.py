from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from apps.manager.decorators import staff_login_required
from apps.core.models import Users
from apps.manager.forms.staffs import *


@staff_login_required
def staffs_page(request):
    staffs = Users.objects.filter(groups__name='Personel')
    return render(request, 'manager/staffs/list.html', context={
        'staffs': staffs
    })


@staff_login_required
def staff_create(request):
    if request.method == 'POST':
        form = StaffCreateForm(request.POST, request.FILES)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.is_staff = True
            staff.save()
            group = Group.objects.get(name='Personel')
            group.user_set.add(staff)
            messages.success(request, 'Personel Başarıyla Eklendi')
            return redirect('admin_staffs_page')
    else:
        form = StaffCreateForm()
    return render(request, 'manager/staffs/create.html', context={
        'form': form
    })


@staff_login_required
def staff_update(request, pk):
    staff = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personel başarıyla güncellendi')
            return redirect('admin_staffs_page')
    else:
        form = StaffUpdateForm(instance=staff)
    return render(request, 'manager/staffs/update.html', context={
        'form': form,
        'staff': staff
    })


@staff_login_required
def staff_delete(request, pk):
    staff = get_object_or_404(Users, pk=pk).delete()
    if staff:
        messages.success(request, 'Personel Başarıyla Silindi')
        return redirect('admin_staffs_page')
