# Generated by Django 4.1.5 on 2023-01-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0016_alter_weapon_long_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='group',
            field=models.CharField(choices=[('Zwykła', 'Zwykła'), ('Dwuręczna', 'Dwuręczna'), ('Kawaleryjska', 'Kawaleryjska'), ('Korbacz', 'Korbacz'), ('Parująca', 'Parująca'), ('Szermiercza', 'Szermiercza')], default=('Ordinary', 'Zwykła'), max_length=30),
        ),
    ]
