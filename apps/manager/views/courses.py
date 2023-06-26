from django.shortcuts import render, get_object_or_404, redirect
from apps.core.models import Courses, CourseCategories
from apps.manager.forms.courses import CourseForm, CourseCategoryForm
from django.contrib import messages


def course_categories_page(request):
    course_categories = CourseCategories.objects.all()
    return render(request, 'manager/courses/categories/list.html', context={
        'course_categories': course_categories
    })


def course_category_create(request):
    if request.method == 'POST':
        form = CourseCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kurs kategorisi başarıyla eklendi')
            return redirect('admin_course_categories_page')
    else:
        form = CourseCategoryForm()
    return render(request, 'manager/courses/categories/create.html', {
        'form': form
    })


def course_category_update(request, pk):
    course_category = get_object_or_404(CourseCategories, pk=pk)
    if request.method == 'POST':
        form = CourseCategoryForm(request.POST, request.FILES, instance=course_category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kurs kategorisi başarıyla güncellendi')
            return redirect('admin_course_categories_page')
    else:
        form = CourseCategoryForm(instance=course_category)
    return render(request, 'manager/courses/categories/update.html', {
        'course_category': course_category,
        'form': form
    })


def course_category_delete(request, pk):
    course_category = get_object_or_404(CourseCategories, pk=pk).delete()
    if course_category:
        messages.success(request, 'Kurs kategorisi başarıyla silindi')
        return redirect('admin_course_categories_page')


def courses_page(request):
    courses = Courses.objects.all()
    return render(request, 'manager/courses/list.html', context={
        'courses': courses
    })


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kurs başarıyla oluşturuldu')
            return redirect('admin_courses_page')
    else:
        form = CourseForm()
    return render(request, 'manager/courses/create.html', context={
        'form': form
    })


def course_update(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kurs başarıyla güncellendi')
            return redirect('admin_courses_page')
    else:
        form = CourseForm(instance=course)
    return render(request, 'manager/courses/update.html', {
        'course': course,
        'form': form
    })


def course_delete(request, pk):
    course = get_object_or_404(Courses, pk=pk).delete()
    if course:
        messages.success(request, 'Kurs başarıyla silindi')
        return redirect('admin_courses_page')
