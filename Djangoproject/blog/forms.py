from django import forms
from .models import Comment


class CommentForm(forms.Form):
    new_comment = forms.CharField(
        label='New Comment',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Write a comment...'})
        )


class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
