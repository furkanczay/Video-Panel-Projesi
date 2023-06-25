from apps.core.models import Users
from django.contrib.auth.admin import UserCreationForm, UserChangeForm
from django.forms.widgets import Textarea, TextInput, Select, DateInput, FileInput, NumberInput, \
    SelectMultiple


class InstructorCreateForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar', 'country']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'birth_date': DateInput(attrs={'class': 'form-control', 'data-mask': '00/00/0000'}),
            'bio': Textarea(attrs={'class': 'form-control', 'data-bs-toggle': 'autosize'}),
            'avatar': FileInput(attrs={'class': 'form-control'}),
            'country': Select(attrs={'class': 'form-select'}),
        }


class InstructorUpdateForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar', 'country', 'groups']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'birth_date': DateInput(attrs={'class': 'form-control', 'data-mask': '00/00/0000'}),
            'bio': Textarea(attrs={'class': 'form-control', 'data-bs-toggle': 'autosize'}),
            'avatar': FileInput(attrs={'class': 'form-control'}),
            'country': Select(attrs={'class': 'form-select'}),
            'groups': SelectMultiple(attrs={'class': 'form-select', 'type': 'text', 'id': 'select-states'}),
        }
