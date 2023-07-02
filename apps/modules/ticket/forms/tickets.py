from django import forms
from django.contrib.auth import get_user_model
from apps.modules.ticket.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'content', 'priority', 'category']