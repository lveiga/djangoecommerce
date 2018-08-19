from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    texts = {
        'Lorem ipsum dolor sit amet',
        'consectetur adipisicing elit',
        'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    }
    context = {
        'title': 'Django E-Commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)