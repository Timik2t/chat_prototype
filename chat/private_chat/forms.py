from django import forms
from private_chat.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('dialog', 'sender', 'text',)
