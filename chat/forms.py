from django import forms
from . import models


class MemberChatForm(forms.ModelForm):

    class Meta:
        model = models.Member
        fields = []


class MessageSendForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = ['text']
        widgets = {
            'text': forms.TextInput
        }

