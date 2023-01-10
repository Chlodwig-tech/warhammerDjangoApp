from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print('POST')
        if form.is_valid():
            print('valid')
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('/auth/login')

        messages.error(request, 'Unsuccessful registration. Invalid information')

    form = NewUserForm()
    context = {
        'register_form' : form
    }
    return render(request, 'register.html', context)