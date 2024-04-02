from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Success! Happy Shopping.')
            return redirect('core:home')
        else:
            messages.error(request,'Registration Failed, Try Again!')
    form=RegisterForm()
    return render(request,'userauth/register.html',{
        'form':form,
    })

def login(request):
    return render(request,'userauth/login.html')