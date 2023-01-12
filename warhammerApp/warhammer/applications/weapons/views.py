from django.shortcuts import render, redirect, get_object_or_404
from utilities.authenticators import when_logged_in

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
def weapon_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            print(form.errors)
    form = WeaponForm()
    context = {
        'form' : form
    }
    return render(request, 'weapons/weapon_create.html', context)

@when_logged_in
def weapon_melee_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MeleeWeaponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            print(form.errors)
    form = MeleeWeaponForm()
    context = {
        'form' : form
    }
    return render(request, 'weapons/weapon_create.html', context)

@when_logged_in
def weapon_range_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = RangeWeaponForm(request.POST)
        if form.is_valid():
            weapon = form.save()
            weapon.is_melee = False
            weapon.save()
            return redirect('../')
        else:
            print(form.errors)
    form = RangeWeaponForm()
    context = {
        'form' : form
    }
    return render(request, 'weapons/weapon_create.html', context)

@when_logged_in
def weapon_detail_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Weapon, id=id)
    context = {
        "obj" : obj
    }
    return render(request, 'weapons/weapon_detail.html', context)

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

@when_logged_in
def weapon_delete_view(request, id, *args, **kwargs):
    print('eloo')
    obj = get_object_or_404(Weapon, id=id)
    if request.method == 'POST':
        print('usuwanie')
        obj.delete()
        return redirect('../')
    context = {
        "obj" : obj
    }
    return render(request, 'weapons/weapon_delete.html', context)