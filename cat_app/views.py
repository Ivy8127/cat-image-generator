from django.shortcuts import render
from django.http import HttpResponse
from .services import cat




def home(request):
    context = {'cat': cat}
    return render(request,'home.html',context)
