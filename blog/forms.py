from django import forms

from blog.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {"content": "Add commentary"}