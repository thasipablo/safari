# Generated by Django 3.2.8 on 2021-10-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0007_alter_programme_heure_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='heure_depart',
            field=models.TimeField(),
        ),
    ]
