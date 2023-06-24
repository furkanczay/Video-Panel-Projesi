from django.forms import ModelForm
from apps.manager.models import GeneralSettings, LinksSettings


class GeneralSettingsForm(ModelForm):
    class Meta:
        model = GeneralSettings
        fields = '__all__'
