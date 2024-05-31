from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content',]
        widgets = {
            'message': forms.Textarea(attrs={
                'class':'pb-6 w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
        }