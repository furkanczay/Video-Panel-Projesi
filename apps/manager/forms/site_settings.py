from django.forms import ModelForm
from apps.manager.models import GeneralSettings, LinksSettings


class GeneralSettingsForm(ModelForm):
    class Meta:
        model = GeneralSettings
        exclude = ['site_version', 'site_developers']
