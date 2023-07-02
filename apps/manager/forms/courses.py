from django.forms import ModelForm
from apps.core.models import Courses, CourseCategories, Classroom


class CourseCategoryForm(ModelForm):
    class Meta:
        model = CourseCategories
        fields = ['name']


class CourseForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'category']


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'course', 'period', 'instructor']

