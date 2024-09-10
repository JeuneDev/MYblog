from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

from django.contrib.auth.views import LoginView
from .forms import LoginForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:article_list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
