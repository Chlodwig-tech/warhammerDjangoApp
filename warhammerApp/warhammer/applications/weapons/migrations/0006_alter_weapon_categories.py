# Generated by Django 4.1.5 on 2023-01-11 21:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0005_remove_weapon_categories_weapon_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('is_armour_piercing', 'is_armour_piercing'), ('is_balanced', 'is_balanced'), ('is_defensive', 'is_defensive'), ('is_experimental', 'is_experimental'), ('is_fast', 'is_fast'), ('is_precise', 'is_precise'), ('is_pummeling', 'is_pummeling'), ('is_shrapnel', 'is_shrapnel'), ('is_slow', 'is_slow'), ('is_snare', 'is_snare'), ('is_tiring', 'is_tiring'), ('is_unreliable', 'is_unreliable')], max_length=160),
        ),
    ]