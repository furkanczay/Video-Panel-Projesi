from django import forms
from apps.core.models import Videos, Classroom
from django.utils.translation import gettext_lazy as _


class VideoUpload(forms.ModelForm):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.none(), label=_('Sınıf'))

    class Meta:
        model = Videos
        fields = ['title', 'description', 'video_file', 'link', 'classroom']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['classroom'].queryset = Classroom.objects.filter(instructor=user)

