from django import forms
from .models import Product_Review


Product_Rating = (
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★'),
)

class Product_Review_Form(forms.ModelForm):
    class Meta:
        model = Product_Review
        fields = ['rating', 'review']

    review = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control my-3 py-1 rounded rounded-3',
        'placeholder': 'Review..'
    }))

    rating = forms.ChoiceField(choices=Product_Rating, widget=forms.Select(attrs={
        'class': 'form-select my-3 py-1 rounded rounded-3',
    }))
