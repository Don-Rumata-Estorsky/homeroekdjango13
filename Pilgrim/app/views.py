from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *

from django.http import JsonResponse
import random


def loggining(request):
    if request.user.is_authenticated:
        return redirect('yeslog')
    else:
        return render(request, 'nelog.html')
    
def nelog(request):
    return render(request, 'nelog.html')
    

