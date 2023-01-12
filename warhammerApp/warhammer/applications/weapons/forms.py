from django import forms

from .models import Weapon, GROUP, CATEGORIES, AVAILABILITY, RELOAD

class WeaponForm(forms.ModelForm):
    name    = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nazwa"}))
    description = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={"placeholder": "Opis"}))
    cost_gc = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Cena zk (złote korony)"}))
    cost_s  = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "s (szylingi)"}))
    cost_p  = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "p (pensy)"}))
    enc     = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Obciążenie"}))
    group   = forms.ChoiceField(choices=GROUP, label='Kategoria ')
    damage  = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Siła broni (jeśli S, to wpisz 0, jeśli S-2, to wpisz -2"}))
    availability   = forms.ChoiceField(choices=AVAILABILITY, label='Dostępność')
    short_range    = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Zasięg krótki [m]"}))
    long_range    = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Zasięg długi [m]"}))
    #reload_in_actions    = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Przeładowanie / ilość akcji"}))
    reload_in_actions = forms.ChoiceField(choices=RELOAD, label='Przeładowanie w akcjach')
    is_melee = forms.BooleanField(required=False, label='Broń biała')
    is_two_handed = forms.BooleanField(required=False, label='Wymaga do użycia dwóch rąk')
    is_damage_strength_depend = forms.BooleanField(required=False, label='Siła broni zależy od siły wojownika')
    qualities = forms.MultipleChoiceField(
        required=False,
        label='Cechy oręża',
        widget = forms.SelectMultiple(attrs={
            'class' : 'quality',
            'id' : 'chkveg',
            'multiple' : 'multiple',
            'data-none-selected-text' : 'xdd'
        }),
        choices=CATEGORIES,
    )

    class Meta:
        model = Weapon
        fields = '__all__'

class MeleeWeaponForm(forms.ModelForm):
    name    = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nazwa"}))
    description = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={"placeholder": "Opis"}))
    cost_gc = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Cena zk (złote korony)"}))
    cost_s  = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "s (szylingi)"}))
    cost_p  = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "p (pensy)"}))
    enc     = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Obciążenie"}))
    group   = forms.ChoiceField(choices=GROUP, label='Kategoria ')
    damage  = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Siła broni (jeśli S, to wpisz 0, jeśli S-2, to wpisz -2"}))
    availability   = forms.ChoiceField(choices=AVAILABILITY, label='Dostępność')
    is_two_handed = forms.BooleanField(required=False, label='Wymaga do użycia dwóch rąk')
    is_damage_strength_depend = forms.BooleanField(required=False, label='Siła broni zależy od siły wojownika')
    qualities = forms.MultipleChoiceField(
        required=False,
        label='Cechy oręża',
        widget = forms.SelectMultiple(attrs={
            'class' : 'quality',
            'id' : 'chkveg',
            'multiple' : 'multiple',
            'data-none-selected-text' : 'xdd'
        }),
        choices=CATEGORIES,
    )

    class Meta:
        model = Weapon
        fields = (
            'name',
            'cost_gc',
            'cost_s',
            'cost_p',
            'enc',
            'group',
            'damage',
            'is_two_handed',
            'is_damage_strength_depend',
            'availability',
            'description',
            'qualities'
        )

class RangeWeaponForm(forms.ModelForm):
    name    = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nazwa"}))
    description = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={"placeholder": "Opis"}))
    cost_gc = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Cena zk (złote korony)"}))
    cost_s  = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "s (szylingi)"}))
    cost_p  = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "p (pensy)"}))
    enc     = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Obciążenie"}))
    group   = forms.ChoiceField(choices=GROUP, label='Kategoria ')
    damage  = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Siła broni (jeśli S, to wpisz 0, jeśli S-2, to wpisz -2"}))
    availability   = forms.ChoiceField(choices=AVAILABILITY, label='Dostępność')
    short_range    = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Zasięg krótki [m]"}))
    long_range    = forms.IntegerField(required=False, label='', widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Zasięg długi [m]"}))
    reload_in_actions = forms.ChoiceField(choices=RELOAD, label='Przeładowanie w akcjach')
    is_two_handed = forms.BooleanField(required=False, label='Wymaga do użycia dwóch rąk')
    is_damage_strength_depend = forms.BooleanField(required=False, label='Siła broni zależy od siły wojownika')
    qualities = forms.MultipleChoiceField(
        required=False,
        label='Cechy oręża',
        widget = forms.SelectMultiple(attrs={
            'class' : 'quality',
            'id' : 'chkveg',
            'multiple' : 'multiple',
            'data-none-selected-text' : 'xdd'
        }),
        choices=CATEGORIES,
    )

    class Meta:
        model = Weapon
        fields = (
            'name',
            'cost_gc',
            'cost_s',
            'cost_p',
            'enc',
            'group',
            'damage',
            'short_range',
            'long_range',
            'reload_in_actions',
            'is_two_handed',
            'is_damage_strength_depend',
            'availability',
            'description',
            'qualities',
        )