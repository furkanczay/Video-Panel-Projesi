from django import forms
from apps.core.models import Courses, Users
from django.utils.translation import gettext_lazy as _


class VideoFilterForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Courses.objects.all(), required=False, label=_('Kurs'))
    instructor = forms.ModelChoiceField(queryset=Users.objects.filter(groups__name='Eğitmen'), required=False, label=_('Eğitmen'))
