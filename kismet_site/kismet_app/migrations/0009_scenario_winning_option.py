# Generated by Django 4.2.dev20221107192353 on 2023-01-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0008_remove_scenario_winning_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='winning_option',
            field=models.CharField(default='add', max_length=200),
        ),
    ]
