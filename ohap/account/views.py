from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == "POST":

        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid:
            sign_up_form.save()
            return redirect('index')

        else:
            return redirect('sign_up')

    sign_up_form = UserCreationForm()
    return render(request,'registration/sign_up.html',{'sign_up_form':sign_up_form})

# Create your views here.
