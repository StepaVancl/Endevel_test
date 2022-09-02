from django import forms


class BlogForm(forms.Form):
    tag_id = forms.IntegerField()

