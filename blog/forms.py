from django import forms

from .models import Post

class SubmitForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)