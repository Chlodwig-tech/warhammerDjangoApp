# Generated by Django 4.1.5 on 2023-01-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0024_weapon_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
