from django.shortcuts import  render

# Create your views here.

from utilities.authenticators import when_logged_in

@when_logged_in
def welcome_view(request, *args, **kwargs):  
    return render(request, 'index.html', {})