from django import forms
from .models import Review


RATING_CHOISES = [(i, str(i)) for i in range(1, 5)]


class UserReviewAddForm(forms.Form):

    rating = forms.TypedChoiceField(
        choices=RATING_CHOISES,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
    text = Review.text



