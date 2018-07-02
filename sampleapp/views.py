from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse
from django.contrib.auth import authenticate


def login(request):
    return render(request, 'login.html')


def login_failed(request):
    return render(request, 'login_fail.html')


def login_submit(request):
    user = request.POST['username']
    pwd = request.POST['password']
    request.session['user'] = user
    user = authenticate(username=user, password=pwd)
    if user is not None:
        return HttpResponseRedirect(reverse('sampleapp:select'))
    else:
        return HttpResponseRedirect(reverse('sampleapp:login_failed'))


def select(request):
    return render(request, 'select.html')


def output(request):
    context = {
        'user': request.session['user'],
        'fruit': request.GET['fruit']
    }
    return render(request, 'output.html', context)
