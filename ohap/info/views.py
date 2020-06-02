from django.shortcuts import render
from .models import Beer

def info(request):
    all_Beer = Beer.objects.all()
    context = {'take_all_Beer' : all_Beer}

    return render(request, 'info.html', context)

# def like(request):
#     temp_target = request.POST.get('target')

#     return render(request, 'info.html', )
    




# Create your views here.
