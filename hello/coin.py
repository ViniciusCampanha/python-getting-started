from django.shortcuts import render        
from django.http import HttpResponse
from django.http import JsonResponse

from  random import choice

# Create your views here.
def flip(request):
    return JsonResponse({'Caiu na moeda: ':choice(['Cara', 'Coroa'])})

