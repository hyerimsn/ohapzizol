from django.shortcuts import render, get_object_or_404
from .models import Beer
from django.views.generic import RedirectView

def info(request):
    all_Beer = Beer.objects.all()
    context = {'take_all_Beer' : all_Beer}

    return render(request, 'info.html', context)

# class PostLikeRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         slug= self.kwargs.get("slug")
#         print(slug)
#         obj = get_object_or_404(Beer, slug=slug)
#         url_ = obj.get_absolute_url()
#         user = self.request.user
#         if user.is_authenticated():
#             if user in obj.likes.all()
#             obj.likes.add(user)
#         return url_ 

# def like(request, beer_id):
#     mylike = Beer.objects.get(pk=beer_id)
#     if Beer.like.filter(id=user.id).exists():
#         Beer.like.remove(user)
#     else:
#         Beer.like.add(user)
#     COUNTA(like)

#     context = {}
#     return render(request, 'info.html', context)

    
    




# Create your views here.
