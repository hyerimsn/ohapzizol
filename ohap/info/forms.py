from django import forms
from .models import Beer

class beerform(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ("__all__")

# class likeform(forms.ModelForm):
#     class Meta:
#         model = Like
#         fiels = ('body',)
