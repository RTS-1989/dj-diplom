from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm


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


def user_logout(request):
    logout(request)
    return redirect('/index.html')
