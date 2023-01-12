# Generated by Django 4.1.5 on 2023-01-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0003_weapon_is_armour_piercing_weapon_is_balanced_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeaponCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_armour_piercing',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_balanced',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_defensive',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_experimental',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_fast',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_precise',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_pummeling',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_shrapnel',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_slow',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_snare',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_special',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_tiring',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='is_unreliable',
        ),
        migrations.AddField(
            model_name='weapon',
            name='categories',
            field=models.ManyToManyField(to='weapons.weaponcategory'),
        ),
    ]
