from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/zero.html')


def about(request):
    return render(request, 'main/second.html')


def third(request):
    return render(request, 'main/third.html')


def zero(request):
    return render(request, 'main/first.html')
