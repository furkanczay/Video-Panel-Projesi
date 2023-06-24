from apps.core.models import Users
from django.contrib.auth.admin import UserCreationForm, UserChangeForm
from django import forms


# STUDENT FORMS
# STUDENT CREATE FORM
class StudentForm(UserCreationForm):
    student_number = forms.CharField(required=True)
    birth_date = forms.DateField(widget=forms.DateTimeInput(attrs={'data-mask': '00/00/0000'}))

    class Meta:
        model = Users
        fields = ['student_number', 'first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar', 'country']


# STUDENT UPDATE FORM
class StudentUpdateForm(UserChangeForm):
    student_number = forms.CharField(required=True)
    birth_date = forms.DateField()

    class Meta:
        model = Users
        fields = ['student_number', 'first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar', 'country',
                  'groups']
