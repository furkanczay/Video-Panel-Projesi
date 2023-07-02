from django import forms
from apps.core.models import Users, UserSocialLinks


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'country', 'birth_date', 'avatar')
        widgets={
            'birth_date': forms.DateInput(attrs={'type': 'text', 'datepicker': 'datepicker'}),
        }


class SocialLinksForm(forms.ModelForm):
    class Meta:
        model = UserSocialLinks
        fields = ('title', 'link')