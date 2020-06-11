from django.shortcuts import render,redirect,get_object_or_404
from .forms import CommentForm,ReCommentForm
from .models import Publist,Menulist,Menudetail,Comment,ReComment,User


# Create your views here.

def index(request):
    a = Publist.objects.all()
    return render(request,'index.html',{'a':a})

def pub(request, mypub_id):
    mypub = get_object_or_404(Publist,pk=mypub_id)
    menu = Menulist.objects.filter(Publist=mypub)
    #댓글
    mycom_form = CommentForm()
    myrecom_form = ReCommentForm()
    context = {'comment_form':mycom_form,'mypub':mypub,'menu':menu,'recomment_form':myrecom_form}
    return render(request, 'pub.html', context)

def beer(request, mymenu_id):
    mymenu = get_object_or_404(Menulist,pk=mymenu_id)
    mybeer = Menudetail.objects.filter(menulist=mymenu)
    # ilike = Menudetail.likes
    mymenu_id = mymenu_id
    context ={'mymenu':mymenu,'mybeer':mybeer,'mymenu_id':mymenu_id}
    return render(request, 'beer.html', context)


def create_comment(request, mypub_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        a= filled_form.save(commit=False)
        a.author=request.user
        a.save()
    return redirect('pub', mypub_id)

def delete_comment(request, com_id,mypub_id):
    mycom = Comment.objects.get(id = com_id)
    mycom.delete()
    return redirect('pub', mypub_id)
    
def create_recomment(request, mypub_id):
    filled_form = ReCommentForm(request.POST) 

    if filled_form.is_valid():
        a= filled_form.save(commit=False)
        a.author=request.user
        a.save()
    return redirect('pub', mypub_id)

def delete_recomment(request, recom_id, mypub_id):
    myrecom = ReComment.objects.get(id = recom_id)
    myrecom.delete()
    return redirect('pub', mypub_id)

def like(request, mylike_id, mymenu_id):
    user = request.user
    print(mylike_id)
    if request.method == 'POST' and user.is_authenticated:
        # user = request.user
        # mylike = request.POST.get('pk', None)
        ilike = Menudetail.objects.get(pk = mylike_id)
        if ilike.likes.filter(id = user.id).exists():
            ilike.likes.remove(user)
        else:
            ilike.likes.add(user)
    else:
        return render(request,'index.html', {'login_flag' : True})
    context = {'likes_count' : ilike.likes}
    return redirect('beer', mymenu_id)
