from django import forms
from .models import Review


RATING_CHOISES = [(i, str(i)) for i in range(1, 5)]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['name', 'text']




