from django import forms
from . import models


class MemberChatForm(forms.ModelForm):

    class Meta:
        model = models.Member
        fields = []


class MessageSendForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = ['text', 'photo']
        widgets = {
            'text': forms.TextInput,
            'photo': forms.FileInput(attrs={'class': 'message-image-input'})
        }

