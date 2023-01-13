from django.shortcuts import render, redirect, get_object_or_404

from utilities.authenticators import when_logged_in
from utilities.view_decorators import create_view, delete_view, detail_view

from .models import Weapon
from .forms import WeaponForm, MeleeWeaponForm, RangeWeaponForm

# Create your views here.

@when_logged_in
def weapon_list_view(request, *args, **kwargs):
    melee_weapons = Weapon.objects.filter(is_melee=True)
    range_weapons = Weapon.objects.filter(is_melee=False)
    context = {
        'melee_weapons' : melee_weapons,
        'range_weapons' : range_weapons
    }
    return render(request, 'weapons/weapon_list.html', context)

@when_logged_in
@detail_view(Weapon)
def weapon_detail_view(request, context, *args, **kwargs):
    return render(request, 'weapons/weapon_detail.html', context)

@when_logged_in
@create_view(WeaponForm)
def weapon_create_view(request, context, *args, **kwargs):
    return render(request, 'weapons/weapon_create.html', context)

@when_logged_in
@create_view(MeleeWeaponForm)
def weapon_melee_create_view(request, context, *args, **kwargs):
    return render(request, 'weapons/weapon_create.html', context)

@when_logged_in
@create_view(RangeWeaponForm)
def weapon_range_create_view(request, context, *args, **kwargs):
    return render(request, 'weapons/weapon_create.html', context)

@when_logged_in
@delete_view(Weapon)
def weapon_delete_view(request, context, *args, **kwargs):
    return render(request, 'weapons/weapon_delete.html', context)

@when_logged_in
def weapon_edit_view(request, id, *args, **kwargs):
    obj = Weapon.objects.get(id=id)
    formTemplate = MeleeWeaponForm if obj.is_melee else RangeWeaponForm
    form = formTemplate(request.POST or None, instance=obj) 
    if form.is_valid():
        form.save()
        form = formTemplate()
        return redirect('../')
    context = {
        'form' : form
    }
    return render(request, "weapons/weapon_create.html", context)