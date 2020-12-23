from django import forms
from . import models


class addProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'description', 'slug']
