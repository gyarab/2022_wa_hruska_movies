from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class CommentForm(forms.Form):
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Egor"})
    )
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 5, "class": "form-control"})
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=False,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )