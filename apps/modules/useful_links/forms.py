from django import forms
from .models import UsefulLinks

class UsefulLinksForm(forms.ModelForm):
    class Meta:
        model = UsefulLinks
        fields = ['title', 'link', 'description']
        error_messages = {
            'title': {
                'required': 'Başlık alanı boş bırakılamaz',
                'max_length': 'Başlık alanı en fazla 255 karakter olabilir'
            },
            'link': {
                'required': 'Link alanı boş bırakılamaz',
                'max_length': 'Link alanı en fazla 255 karakter olabilir'
            },
            'description': {
                'required': 'Açıklama alanı boş bırakılamaz'
            }
        }