from django import forms
from .models import Comment,ReComment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','body','post')


class ReCommentForm(forms.ModelForm):

    
    class Meta:
        model = ReComment
        fields = ('author','body','comment')