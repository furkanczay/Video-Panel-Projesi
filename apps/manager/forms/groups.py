from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.forms.widgets import TextInput, SelectMultiple


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'permissions': SelectMultiple(attrs={'class': 'form-select', 'type': 'text', 'id': 'select-states'}),
        }
        error_messages = {
            'name': {
                'unique': 'Bu isimde zaten bir grup mevcut'
            }
        }


class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'permissions': SelectMultiple(attrs={'class': 'form-select'}),
        }
