from django.shortcuts import render        
from django.http import HttpResponse

from  random import choice

# Create your views here.
def flip(request):
    return render(request, choice(['Cara', 'Coroa']))

