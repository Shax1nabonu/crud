# Generated by Django 4.2.5 on 2023-09-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(),
        ),
    ]
