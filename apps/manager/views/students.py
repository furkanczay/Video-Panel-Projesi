from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from apps.manager.forms.students import StudentForm, StudentUpdateForm
from apps.core.models import Users


# STUDENTS VIEWS
@login_required()
@staff_member_required()
def students_page(request):
    students = Users.objects.filter(groups__name='Öğrenci')
    return render(request, 'manager/students/list.html', context={
        'students': students
    })


@login_required()
@staff_member_required()
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


@login_required()
@staff_member_required()
def student_update(request, pk):
    student = get_object_or_404(Users, pk=pk)
    initial_data = {'classroom': student.student_classroom.first()}
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student, initial=initial_data)
        if form.is_valid():
            form.save()
            student.student_classroom.clear()  # Öğrencinin bağlı olduğu eski sınıfları kaldır
            selected_classroom = form.cleaned_data['classroom']
            student.student_classroom.add(selected_classroom)
            messages.success(request, 'Öğrenci başarıyla güncellendi')
            return redirect('admin_students_page')
    else:
        form = StudentUpdateForm(instance=student, initial=initial_data)
    return render(request, 'pages/users/students/update.html', context={
        'form': form,
        'student': student
    })


@login_required()
@staff_member_required()
def student_delete(request, pk):
    student = get_object_or_404(Users, pk=pk).delete()
    if student:
        messages.success(request, 'Öğrenci Başarıyla Silindi')
        return redirect('admin_students_page')
