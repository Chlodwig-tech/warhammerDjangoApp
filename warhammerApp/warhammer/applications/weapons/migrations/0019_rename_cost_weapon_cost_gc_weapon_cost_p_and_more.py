# Generated by Django 4.1.5 on 2023-01-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0018_alter_weapon_availability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='cost',
            new_name='cost_gc',
        ),
        migrations.AddField(
            model_name='weapon',
            name='cost_p',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weapon',
            name='cost_s',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]