# Generated by Django 3.2.4 on 2022-07-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
