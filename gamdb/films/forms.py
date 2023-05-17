from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class CommentForm(forms.Form):
    author = forms.CharField(required=False)
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5}))
    rating = forms.IntegerField(required=False,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )