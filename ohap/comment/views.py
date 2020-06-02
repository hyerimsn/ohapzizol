from django.shortcuts import render, redirect, get_object_or_404
from .forms import TempForm,CommentForm,ReCommentForm
from .models import Temp,Comment,ReComment
from django.http import Http404

def dongyeop(request, temp_id):
    # temp = get_object_or_404(Temp, pk=temp_id)
    try:
        temp = Temp.objects.get(pk=temp_id)
    except:
        raise Http404
    
    mycom_form = CommentForm()
    myrecom_form = ReCommentForm()
    context = {'comment_form':mycom_form, 'temp':temp,'recomment_form':myrecom_form}
    return render(request, 'pub.html',context)

def create_comment(request, temp_id):
    filled_form = CommentForm(request.POST) 

    if filled_form.is_valid():
        filled_form.save()
    
    return redirect('dongyeop', temp_id)


def delete_comment(request, com_id,temp_id):
    mycom = Comment.objects.get(id = com_id)
    mycom.delete()
    return redirect('dongyeop', temp_id)

def create_recomment(request, temp_id):
    filled_form = ReCommentForm(request.POST) 

    if filled_form.is_valid():
        filled_form.save()
    
    return redirect('dongyeop', temp_id)