from django.forms import ModelForm
from apps.core.models import Courses, CourseCategories


class CourseCategoryForm(ModelForm):
    class Meta:
        model = CourseCategories
        fields = ['name']



class CourseForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'category']
