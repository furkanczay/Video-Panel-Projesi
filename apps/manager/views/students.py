from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from apps.manager.decorators import staff_login_required
from apps.manager.forms.students import StudentForm, StudentUpdateForm
from apps.core.models import Users


# STUDENTS VIEWS
@staff_login_required
def students_page(request):
    students = Users.objects.filter(groups__name='Öğrenci')
    return render(request, 'manager/students/list.html', context={
        'students': students
    })


@staff_login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            group = Group.objects.get(name='Öğrenci')
            group.user_set.add(student)
            messages.success(request, 'Öğrenci başarıyla kaydedildi')
            return redirect('admin_students_list')
    else:
        form = StudentForm()
    return render(request, 'manager/students/create.html', context={
        'form': form
    })


@staff_login_required
def student_update(request, pk):
    student = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Öğrenci başarıyla güncellendi')
            return redirect('admin_students_list')
    else:
        form = StudentUpdateForm(instance=student)
    return render(request, 'manager/students/update.html', context={
        'form': form,
        'student': student
    })


@staff_login_required
def student_delete(request, pk):
    student = get_object_or_404(Users, pk=pk).delete()
    if student:
        messages.success(request, 'Öğrenci Başarıyla Silindi')
        return redirect('admin_students_list')
