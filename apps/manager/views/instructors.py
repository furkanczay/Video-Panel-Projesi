from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from apps.manager.decorators import staff_login_required
from apps.core.models import Users
from apps.manager.forms.instructors import *


# INSTRUCTORS VIEWS
@staff_login_required
def instructors_page(request):
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return render(request, 'manager/instructors/list.html', context={
        'instructors': instructors
    })


@staff_login_required
def instructor_create(request):
    if request.method == 'POST':
        form = InstructorCreateForm(request.POST, request.FILES)
        if form.is_valid():
            instructor = form.save()
            group = Group.objects.get(name='Eğitmen')
            group.user_set.add(instructor)
            messages.success(request, 'Eğitmen Başarıyla Eklendi')
            return redirect('admin_instructors_page')
    else:
        form = InstructorCreateForm()
    return render(request, 'manager/instructors/create.html', context={
        'form': form
    })


@staff_login_required
def instructor_update(request, pk):
    instructor = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = InstructorUpdateForm(request.POST, request.FILES, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Eğitmen başarıyla güncellendi')
            return redirect('admin_instructors_list')
    else:
        form = InstructorUpdateForm(instance=instructor)
    return render(request, 'manager/instructors/update.html', context={
        'form': form,
        'instructor': instructor
    })


@staff_login_required
def instructor_delete(request, pk):
    instructor = get_object_or_404(Users, pk=pk).delete()
    if instructor:
        messages.success(request, 'Eğitmen Başarıyla Silindi')
        return redirect('admin_instructors_list')
