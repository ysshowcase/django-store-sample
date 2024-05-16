from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home from context',
        'content': 'Form to get context'
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("About")

