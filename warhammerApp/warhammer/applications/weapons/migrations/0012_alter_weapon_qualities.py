# Generated by Django 4.1.5 on 2023-01-12 13:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0011_alter_weapon_qualities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='qualities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('is_tiring', 'Ciężki'), ('is_impact', 'Druzgoczący'), ('is_experimental', 'Eksperymentalny'), ('is_shrapnel', 'Odłamkowy'), ('is_pummeling', 'Ogłuszający'), ('is_defensive', 'Parujący'), ('is_slow', 'Powolny'), ('is_precise', 'Precyzyjny'), ('is_armour_pisercing', 'Przebijający zbroję'), ('is_special', 'Specjalny'), ('is_fast', 'Szybki'), ('is_snare', 'Unieruchamiający'), ('is_balanced', 'Wyważony'), ('is_unreliable', 'Zawodny')], max_length=180, null=True),
        ),
    ]
