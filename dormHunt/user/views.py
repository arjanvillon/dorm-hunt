from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from user.forms import RegistrationForm, UserAuthenticationForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    context = {}
    registered = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=raw_password)
            # login(request, user)
            return redirect('user:user_login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user/register.html', context)

def user_login(request):
    context = {}

    user = request.user

    if user.is_authenticated:
        return redirect('home:view_home')

    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:view_home')
        else:
            return HttpResponse('Not signed in!')
    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)

def user_forgot_password(request):
    return render(request, 'user/forgot_password.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:user_login'))