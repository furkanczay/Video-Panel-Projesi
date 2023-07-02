from apps.core.models import Users
from django import forms
from django.contrib.auth.admin import UserCreationForm, UserChangeForm


class StaffCreateForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateTimeInput(attrs={'data-mask': '00/00/0000'}))
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar', 'country']


class StaffUpdateForm(UserChangeForm):
    birth_date = forms.DateField(widget=forms.DateTimeInput(attrs={'data-mask': '00/00/0000'}))
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar', 'country', 'groups']
