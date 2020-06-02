from django import forms
from .models import Temp,Comment,ReComment

class TempForm(forms.ModelForm):
    model = Temp

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body','post')

class ReCommentForm(forms.ModelForm):

    
    class Meta:
        model = ReComment
        fields = ('body','comment',)
