# Generated by Django 4.1.5 on 2023-01-11 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0007_delete_weaponcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='categories',
            new_name='qualities',
        ),
    ]
