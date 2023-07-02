from apps.core.models import Videos
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = '__all__'
