from django import forms


class CommentForm(forms.Form):
    new_comment = forms.CharField(
        label='New Comment',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Write a comment...'})
        )
