from django import forms
from . import models


class MemberChatForm(forms.ModelForm):
    """ Class for forms which adding member to chat """
    class Meta:
        model = models.Member
        fields = []


class MessageSendForm(forms.ModelForm):
    """ Class for forms which using for adding message to chat """
    class Meta:
        model = models.Message
        fields = ['text', 'photo', 'voice']
        widgets = {
            'text': forms.TextInput,
            'photo': forms.FileInput(attrs={'class': 'message-image-input'}),
            'voice': forms.FileInput(attrs={'class': 'message-video-input'}),
        }

