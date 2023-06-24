from django import forms
from apps.core.models import Courses, Classroom
from django.utils.translation import gettext_lazy as _


class VideoFilterForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Courses.objects.all(), required=False, label=_('Kurs'))
