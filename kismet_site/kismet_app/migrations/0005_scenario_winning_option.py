# Generated by Django 4.2.dev20221107192353 on 2023-01-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0004_scenario_option1_scenario_option2_scenario_option3'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='winning_option',
            field=models.CharField(default='add', max_length=200),
        ),
    ]