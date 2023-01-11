from django.shortcuts import render
from utilities.authenticators import when_logged_in

# Create your views here.

@when_logged_in
def welcome_warhammer_view(request, *args, **kwargs):  
    return render(request, 'warhammer/index.html', {})