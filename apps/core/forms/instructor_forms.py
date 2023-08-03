from django import forms
from apps.core.models import Videos, Classroom
from django.utils.translation import gettext_lazy as _


class VideoUpload(forms.ModelForm):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.none(), label=_('Sınıf'))

    class Meta:
        model = Videos
        fields = ['title', 'description', 'video_url', 'link', 'classroom']
        help_texts = {
            'link': 'Eğer ders içeriğinde kullanılan kodları paylaşmak istiyorsanız link ekleyebilirsiniz',
            'video_file': 'Yalnızca .mp4 videolar desteklenmektedir.'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['classroom'].queryset = Classroom.objects.filter(instructor=user)

