# Generated by Django 3.2.7 on 2021-09-20 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_from', models.CharField(max_length=250)),
                ('go_to', models.CharField(max_length=250)),
                ('go_date_time', models.DateTimeField()),
                ('places', models.IntegerField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='agency.agency')),
            ],
        ),
    ]