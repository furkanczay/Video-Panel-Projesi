from django import forms
from apps.core.models import Users


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'country', 'birth_date', 'avatar')
