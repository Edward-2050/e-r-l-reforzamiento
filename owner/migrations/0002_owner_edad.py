# Generated by Django 4.2.7 on 2023-12-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]
