from django import http
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, loginForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user.is_active:
                login(request, user)
                return HttpResponse('Все хорошо')
            else:
                return HttpResponse('Что-то пошло не так(')
        else:
            return HttpResponse('Пользователя с таким логином не существует')
    else:
        form = loginForm()
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form}) 

@login_required
def dashboard(request):
    return render(request, 'main/allChats.html', {'section': 'dashboard'})

# Create your views here.
