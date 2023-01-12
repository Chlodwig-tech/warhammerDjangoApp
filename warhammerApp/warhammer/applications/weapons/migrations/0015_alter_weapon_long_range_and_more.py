# Generated by Django 4.1.5 on 2023-01-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0014_alter_weapon_long_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='long_range',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='reload_in_actions',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='short_range',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]