from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from utilities.authenticators import when_logged_in, when_logged_out

# Create your views here.

@when_logged_out
def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            print('valid')
            user = form.save()
            login(request, user)
            messages.success(request, 'Rejestracja przebiegła pomyślnie')
            return redirect('/login')

        messages.error(request, 'Rejsetracja nie udała się. Podano nieprawidłowe dane.')

    form = NewUserForm()
    context = {
        'register_form' : form
    }
    return render(request, 'register.html', context)

@when_logged_out
def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Jesteś zalogowany jako {username}.")
                return redirect('/welcome')
            messages.error(request,"Nieprawidłowy login lub hasło.")
        else:
            messages.error(request,"Nieprawidłowy login lub hasło.")
            
    form = LoginForm()
    context = {
        'login_form' : form
    }
    return render(request, 'login.html', context)

@when_logged_in
def logout_view(request, *args, **kwargs):
    logout(request)
    messages.info(request, "Wylogowałeś się pomyślnie.")
    return redirect('/welcome')