# Generated by Django 4.1.5 on 2023-01-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('WW', models.IntegerField()),
                ('US', models.IntegerField()),
                ('K', models.IntegerField()),
                ('Odp', models.IntegerField()),
                ('Zr', models.IntegerField()),
                ('Int', models.IntegerField()),
                ('SW', models.IntegerField()),
                ('Ogd', models.IntegerField()),
                ('A', models.IntegerField()),
                ('Zyw', models.IntegerField()),
                ('Sz', models.IntegerField()),
                ('Mag', models.IntegerField()),
                ('PO', models.IntegerField()),
                ('PP', models.IntegerField()),
            ],
        ),
    ]
