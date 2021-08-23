from django import forms
from .models import MessagePrivate


class PrivateMessageForm(forms.ModelForm):
    """ Create private message form with using Django forms ModelForm"""

    class Meta:
        model = MessagePrivate
        fields = ['text', 'photo']
        widgets = {
            'text': forms.TextInput,
            'photo': forms.FileInput(attrs={'class': 'message-image-input'})
        }
