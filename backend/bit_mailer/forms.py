from django import forms
from .models import MailRequest

class MailRequestForm(forms.ModelForm):
    class Meta:
        model = MailRequest
        fields = ['subject', 'recipient', 'from_time', 'to_time', 'date', 'department', 'year', 'content']
