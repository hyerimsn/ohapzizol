from django import forms
from .models import Comment,ReComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','post')
        widgets = {
            'body': forms.TextInput(attrs={'style': 'border-radius: 10px;'}),
            # 'post': forms.CharField(attrs={'style': 'border-radius: 10px'}),
        }

class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('body','comment')
        widgets = {
            'body': forms.TextInput(attrs={'style': 'border-radius: 10px;'}),
        }