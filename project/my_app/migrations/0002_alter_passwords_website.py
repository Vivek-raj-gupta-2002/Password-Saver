# Generated by Django 4.2 on 2023-04-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwords',
            name='website',
            field=models.URLField(),
        ),
    ]
