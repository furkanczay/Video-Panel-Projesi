from django.forms import ModelForm
from apps.core.models import Videos


class VideoUpload(ModelForm):
    class Meta:
        model = Videos
        fields = ['title', 'description', 'video_file', 'link', 'classroom']
