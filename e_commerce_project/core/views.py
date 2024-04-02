from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def home(request):
    
    context = {

    }
    return render(request, 'core/index.html', context)
