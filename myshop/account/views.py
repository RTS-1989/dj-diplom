from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm


def signup_view(request):
    template = 'registration/signup.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'registration/register_done',
                          {'new_user': new_user})
    else:
        form = SignupForm(request.POST)

    context = {
               'user_form': form,
    }

    return render(request, template, context)


def user_logout(request):
    logout(request)
    return redirect('/index.html')
