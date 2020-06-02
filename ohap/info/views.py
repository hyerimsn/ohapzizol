from django.shortcuts import render
from .models import Beer

def info(request):
    all_Beer = Beer.objects.all()
    context = {'take_all_Beer' : all_Beer}

    return render(request, 'info.html', context)


    




# Create your views here.
