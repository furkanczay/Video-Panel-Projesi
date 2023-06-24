from django import forms
from apps.core.models import Videos, Classroom


class VideoUpload(forms.ModelForm):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.none())

    class Meta:
        model = Videos
        fields = ['title', 'description', 'video_file', 'link', 'classroom']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['classroom'].queryset = Classroom.objects.filter(instructor=user)

