# Generated by Django 4.1.4 on 2023-01-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0006_alter_choice_the_scenario'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='choices',
            field=models.ManyToManyField(to='kismet_app.choice'),
        ),
    ]
