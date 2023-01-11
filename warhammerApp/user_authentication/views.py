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
        print('POST')
        if form.is_valid():
            print('valid')
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('/login')

        messages.error(request, 'Unsuccessful registration. Invalid information')

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
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/welcome')
            messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
            
    form = LoginForm()
    context = {
        'login_form' : form
    }
    return render(request, 'login.html', context)

@when_logged_in
def logout_view(request, *args, **kwargs):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/welcome')