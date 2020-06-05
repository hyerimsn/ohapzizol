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
    context = {'comment_form':mycom_form,'mypub':mypub,'menu':menu, 'recomment_form':myrecom_form}
    return render(request, 'pub.html', context)

def beer(request, mymenu_id):
    mymenu = get_object_or_404(Menulist,pk=mymenu_id)
    mybeer = Menudetail.objects.filter(menulist=mymenu)
    context ={'mymenu':mymenu,'mybeer':mybeer}
    return render(request, 'beer.html', context)


def create_comment(request, mypub_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        filled_form.save()

    return redirect('pub', mypub_id)

def delete_comment(request, com_id,mypub_id):
    mycom = Comment.objects.get(id = com_id)
    mycom.delete()
    return redirect('pub', mypub_id)
    
def create_recomment(request, mypub_id):
    filled_form = ReCommentForm(request.POST) 

    if filled_form.is_valid():
        filled_form.save()
    
    return redirect('pub', mypub_id)

def like(request, mylike_id):
    # mylike = get_object_or_404(Menudetail, pk=mylike_id)
    # alist = mylike.objects.filter(likes = request.user)
    
    # ilike = Menudetail.objects.filter(menudetail=mylike)
    # mylike = Menudetail.objects.get(Menudetail,pk=mylike_id)
    # mylike.filter(Menudetail=likes)

    # if request.method == 'POST':
    #     user = request.user
    #     if alist.exists():
    #         mylike.likes.remove(request.user)
    #     else:
    #         mylike.likes.add(user)
    # context = {'likes_count' : mylike.total_likes}

    # return redirect(request, 'beer.html', context)


    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        mylike = request.POST.get('pk', None)
        alist = Menudetail.objects.get(pk = mylike_id)
        if alist.likes.filter(id = user.id).exists():
            alist.likes.remove(user)
        else:
            alist.likes.add(user)
        context = {'likes_count' : alist.likes}
    else :
        return redirect('login')
    
    return render(request,'beer.html',{'context':context})