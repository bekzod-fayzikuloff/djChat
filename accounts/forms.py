from django import forms
from .models import MessagePrivate


class PrivateMessageForm(forms.ModelForm):

    class Meta:
        model = MessagePrivate
        fields = ['text', 'photo']
        widgets = {
            'text': forms.TextInput,
            'photo': forms.FileInput(attrs={'class': 'message-image-input'})
        }