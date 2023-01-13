from django.shortcuts import render, redirect, get_object_or_404

from utilities.authenticators import when_logged_in
from utilities.view_decorators import(
    create_view, delete_view, detail_view, edit_view
)

from .models import Character
from .forms import CharacterForm

# Create your views here.
@when_logged_in
def character_list_view(request, *args, **kwargs):
    context = {
        'objects' : Character.objects.all()
    }
    return render(request, 'characters/character_list.html', context)

@when_logged_in
@detail_view(Character)
def character_detail_view(request, context, *args, **kwargs):
    return render(request, 'characters/character_detail.html', context)

@when_logged_in
@create_view(CharacterForm)
def character_create_view(request, context, *args, **kwargs):
    return render(request, 'characters/character_create.html', context)

@when_logged_in
@delete_view(Character)
def character_delete_view(request, context, *args, **kwargs):
    return render(request, 'characters/character_delete.html', context)

@when_logged_in
@edit_view(Character, CharacterForm)
def character_edit_view(request, context, *args, **kwargs):
    return render(request, 'characters/character_create.html', context)