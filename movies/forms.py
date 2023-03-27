from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from movies.models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    """Формы отзывов"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'captcha')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.TextInput(attrs={'class': 'form-control border'}),
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None,
    )

    class Meta:
        model = Rating
        fields = ('star',)
