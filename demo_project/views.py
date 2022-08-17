from re import template
from django.shortcuts import render 

def index(request):
    """ Index Page"""
    template = 'index.html'
    return render(request, template, {'age':54})