from django import forms


class Post_New_Comment(forms.Form):
    new_comment = forms.CharField(label='post_new_comment', max_length=100)
