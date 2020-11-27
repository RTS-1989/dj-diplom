from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm


def signup_view(request):
    template = 'registration/signup.html'
    message = ''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = SignupForm(request.POST)
            message = 'Введены некорректные данные'
    else:
        form = SignupForm(request.POST)

    context = {
               'form': form,
               'message': message
    }

    return render(request, template, context)


def user_login(request):
    template = 'account/login.html'
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm(request.POST)
            message = 'Введены некорректные данные'
    else:
        form = LoginForm(request.POST)
    context = {
               'form': form,
               'message': message
    }
    return render(request, template, context)
